from TranscriptionStream import TranscriptionStream
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--testing", help="Enable testing mode")
    parser.add_argument("--language", help="Specify the language")
    args = parser.parse_args()

    TESTING =True if args.testing and args.testing == True else False
    LANGUAGE = args.language if args.language else None
    print("Testing mode:", TESTING)
    print("Language:", LANGUAGE)

    serial_port = "/dev/cu.usbserial-210"
    transcription_stream = TranscriptionStream(serial_port=serial_port, testing=TESTING, translation_language=LANGUAGE)
    try:
        transcription_stream.run()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")
        transcription_stream.arduino_sender.ser.close()
        exit()