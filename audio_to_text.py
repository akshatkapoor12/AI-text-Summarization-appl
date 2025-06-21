import whisper
import tempfile

def transcribe_with_whisper(audio_bytes):
    model = whisper.load_model("base")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        result = model.transcribe(f.name)
    return result["text"]

