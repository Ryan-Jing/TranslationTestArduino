import sounddevice as sd
import datetime
import openai
import wavio
import threading
import io
import time

from ArduinoSend import ArduinoSend

class TranscriptionStream():
    def __init__(self, serial_port: str, baudrate= 9600, freq=44100, recording_duration=5, testing=False):
        self.freq = freq
        self.recording_duration = recording_duration
        self.testing = testing
        self.transcription_log = []
        self.arduino_sender = ArduinoSend(serial_port=serial_port, baudrate=baudrate)

    def _record_audio(self):
        # try:
            print('Recording audio...')
            while True:

                if self.testing: 
                    audio_file = open("./test_audio_1.mp3", "rb")
                    time.sleep(5)

                else:
                    filename = "in_memory_file" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ".wav"
                    # Start recording given freq and duration
                    recording = sd.rec(int(self.recording_duration * self.freq), samplerate=self.freq, channels=1)
                    sd.wait()
                    audio_file = io.BytesIO()
                    wavio.write(audio_file, data=recording, rate=self.freq, sampwidth=1)
                    audio_file.seek(0)  # Rewind the file pointer to the beginning
                    audio_file.name = filename # necessary for openai SDK to not throw an error

                transcription_thread = threading.Thread(target=self._transcribe_audio, args=(audio_file,))
                transcription_thread.start()
        
        # except KeyboardInterrupt:
        #     return

    def _transcribe_audio(self, audio_file):
        # try:
            transcript = openai.Audio.transcribe("whisper-1", file=audio_file)
            del audio_file
            self.transcription_log.append(transcript["text"])
            print("Writing to arduino:", transcript["text"])
            self.arduino_sender.write_to_arduino(content=transcript["text"] + " ")
            return

        # except KeyboardInterrupt:
        #     return


    def run(self):
        try:
            recording_thread = threading.Thread(target=self._record_audio)
            recording_thread.start()

            while True:
                pass

        except KeyboardInterrupt:
            stop_threads = True
            # Wait for all threads to finish
            self.arduino_sender.ser.close()
            recording_thread.join()
