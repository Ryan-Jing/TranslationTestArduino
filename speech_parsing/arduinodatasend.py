import serial
import time

# establish a serial connection with the Arduino
ser = serial.Serial('/dev/cu.usbserial-210', 9600)  # Replace with the appropriate port
file_path = 'transcriptions/transcriptions.txt'
previous_word = ""

while True:
    with open(file_path, 'r') as file:
        content = file.read()
        result = content.split()

    if result and result[-1] != previous_word:
        # send the new word using ser.write()
        ser.write(result[-1].encode())
        print("writing", result[-1])
    previous_word = result[-1]  # update previous_word


    time.sleep(0.5)  # wait for 1 second before checking for updates again

ser.close()

'''
def get_last_word():
    with open(file_path, 'r') as file:
        content = file.read()
        if content:
            words = content.split()
            return words[-1] if words else ''
    return ''

'''
'''
last_word = get_last_word()

while True:
    # read the text file and get the current last word
    current_word = get_last_word()

    # check if there is a new word
    if current_word and current_word != last_word:
        # send latest word to the Arduino
        ser.write(current_word.encode())
        # update last word variable
        last_word = current_word

    time.sleep(1)  

ser.close()
'''