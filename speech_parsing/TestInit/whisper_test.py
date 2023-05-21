import whisper

model = whisper.load_model("base")
result = model.transcribe("test_audio_1.mp3")
print(result["text"])
