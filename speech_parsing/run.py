from TranscriptionStream import TranscriptionStream
import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--testing", help="Enable testing mode", action="store_true")
    args = parser.parse_args()

    TESTING=True if args.testing and args.testing == True else False
    print("Testing mode:", TESTING)

    serial_port = "/dev/cu.usbserial-210"
    transcription_stream = TranscriptionStream(serial_port=serial_port, testing=TESTING)
    transcription_stream.run()