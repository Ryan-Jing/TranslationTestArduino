# import sounddevice as sd
# import datetime
# import openai
# import numpy as np

# freq = 44100
# duration = 3  # length of each audio file recording

# print('Recording')

# ts = datetime.datetime.now()
# filename = ts.strftime("%Y-%m-%d %H:%M:%S")  # file names based on time

# # Start recording given freq and duration
# recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
# sd.wait()

# # Convert audio data to a byte array
# audio_data = np.asarray(recording, dtype=np.int16)
# audio_bytes = audio_data.tobytes()

# # Transcribe the audio using OpenAI API
# transcript = openai.Audio.transcribe("whisper-1", file=audio_bytes)
# print(transcript)

import sounddevice as sd
import datetime
import openai
# import scipy.io.wavfile as wav
import wavio
import io

freq = 44100
duration = 5  # length of each audio file recording

print('Recording')

ts = datetime.datetime.now()
filename = ts.strftime("%Y-%m-%d %H:%M:%S")  # file names based on time

# Start recording given freq and duration
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()
wavfile = io.BytesIO()
wavio.write(wavfile, data=recording, rate=freq, sampwidth=1)
wavfile.seek(0)  # Rewind the file pointer to the beginning
wavfile.name="in-memory-wav-file.wav"

# Transcribe the audio using OpenAI API
transcript = openai.Audio.transcribe("whisper-1", file=wavfile)
print(transcript)
