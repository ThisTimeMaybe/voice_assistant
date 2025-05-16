
import os
from utils.recorder import record_audio
from utils.transcriber import transcribe_audio
from utils.responder import get_chatgpt_response
from utils.speaker import speak_text
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("🎙️ Say something! (Recording for 5 seconds...)")
    audio_file = record_audio()
    print("📝 Transcribing...")
    text = transcribe_audio(audio_file)
    print("You said:", text)

    print("🤖 Thinking...")
    reply = get_chatgpt_response(text)
    print("Assistant:", reply)

    print("🗣️ Speaking reply...")
    speak_text(reply)
