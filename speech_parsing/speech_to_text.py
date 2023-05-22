import openai
audio_file = open("./test_audio_1.mp3", "rb")
print(type(audio_file))
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)