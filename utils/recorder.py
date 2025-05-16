
import sounddevice as sd
from scipy.io.wavfile import write
import uuid

def record_audio(duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    filename = f"temp_{uuid.uuid4().hex}.wav"
    write(filename, fs, recording)
    return filename
