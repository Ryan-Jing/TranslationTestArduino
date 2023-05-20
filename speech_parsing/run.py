import subprocess

def start_scripts():
    # Start transcription.py
    subprocess.Popen(['python3', 'transcription.py'])

    # Start recording.py
    subprocess.Popen(['python3', 'recording.py'])

    # Start arduinodatasend.py
    subprocess.Popen(['python3', 'arduinodatasend.py'])