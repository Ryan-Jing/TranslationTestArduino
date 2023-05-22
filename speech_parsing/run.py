#how to make run all three python programs at once :/

from TranscriptionStream import TranscriptionStream

if __name__ == "__main__":
    serial_port = "/dev/cu.usbserial-210"
    transcription_stream = TranscriptionStream(serial_port=serial_port, testing=True)
    transcription_stream.run()