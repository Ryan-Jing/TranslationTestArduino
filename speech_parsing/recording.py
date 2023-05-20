import sounddevice as sd
import wavio as wv
import datetime

freq = 44100
duration = 3 # length of each audio file recording

print('Recording')

while True:

    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d %H:%M:%S") # file names based on time

    # start recording given freq and duration
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    sd.wait()

    # converting to a .wav file
    wv.write(f"./recordings/{filename}.wav", recording, freq, sampwidth=2)