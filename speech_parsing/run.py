from TranscriptionStream import TranscriptionStream

TESTING = False

if __name__ == "__main__":
    serial_port = "/dev/cu.usbserial-210"
    transcription_stream = TranscriptionStream(serial_port=serial_port, testing=TESTING)
    transcription_stream.run()