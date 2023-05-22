import serial

class ArduinoSend():
    def __init__(self, serial_port: str, baudrate: int = 9600):
        self.ser = serial.Serial(port=serial_port, baudrate=baudrate)

    def write_to_arduino(self, content: str):
        self.ser.write(content.encode())
