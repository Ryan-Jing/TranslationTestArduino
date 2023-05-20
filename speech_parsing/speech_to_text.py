import openai
audio_file = open("./speech_parsing/test_audio_1.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)