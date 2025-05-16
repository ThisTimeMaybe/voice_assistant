from flask import Flask, render_template, jsonify

print("✅ Flask basic import successful")

try:
    from utils.recorder import record_audio
    print("✅ recorder imported")
except Exception as e:
    print("❌ recorder import failed:", e)

try:
    from utils.transcriber import transcribe_audio
    print("✅ transcriber imported")
except Exception as e:
    print("❌ transcriber import failed:", e)

try:
    from utils.responder import get_chatgpt_response
    print("✅ responder imported")
except Exception as e:
    print("❌ responder import failed:", e)

try:
    from utils.speaker import speak_text
    print("✅ speaker imported")
except Exception as e:
    print("❌ speaker import failed:", e)

app = Flask(__name__)

@app.route('/')
def index():
    print("📄 Rendering index.html")
    return render_template('index.html')

@app.route('/process', methods=['GET'])
def process_voice():
    try:
        print("🎙️ Recording...")
        audio_file = record_audio()
        print("📝 Transcribing...")
        text = transcribe_audio(audio_file)
        print("🤖 Thinking...")
        reply = get_chatgpt_response(text)
        print("🗣️ Speaking...")
        speak_text(reply)
        return jsonify({"transcript": text, "response": reply})
    except Exception as e:
        print("❌ Error in /process:", e)
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    print("🚀 Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True, use_reloader=False)
