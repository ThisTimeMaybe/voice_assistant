import whisper

model = whisper.load_model("base")  # you can also try "small" or "medium" if you want later

def transcribe_audio(file_path):
    print("🔍 Loading audio for transcription...")
    result = model.transcribe(file_path)
    return result["text"]
