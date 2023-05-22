import sounddevice as sd
import datetime
import openai
import wavio
import threading
import io
import time

FREQ = 44100
DURATION = 10 # length of each audio file recording
TESTING = True

transcription_log = []

def record_audio():
    while True:
        print('Recording')

        if TESTING: 
            audio_file = open("./test_audio_1.mp3", "rb")
            time.sleep(5)

        else:
            filename = "in_memory_file" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".wav"

            # Start recording given freq and duration
            recording = sd.rec(int(DURATION * FREQ), samplerate=FREQ, channels=1)
            sd.wait()
            audio_file = io.BytesIO()
            wavio.write(audio_file, data=recording, rate=FREQ, sampwidth=1)
            audio_file.seek(0)  # Rewind the file pointer to the beginning
            audio_file.name = filename # necessary for openai SDK to not throw an error

        transcription_thread = threading.Thread(target=transcribe_audio, args=(audio_file,))
        transcription_thread.start()

def transcribe_audio(wavfile):
    transcript = openai.Audio.transcribe("whisper-1", file=wavfile)
    transcription_log.append(transcript["text"])
    print(transcription_log)

try:
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    while True:
        pass

except KeyboardInterrupt:
    # Set the flag to signal thread termination
    stop_threads = True
    # Wait for all threads to finish
    recording_thread.join()
