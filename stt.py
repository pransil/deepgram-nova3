import sys
import json
import os
from pathlib import Path
from deepgram import DeepgramClient

API_KEY = os.getenv("DEEPGRAM_API_KEY")

if not API_KEY:
    print("Please set DEEPGRAM_API_KEY")
    sys.exit(1)

if len(sys.argv) < 2:
    print("Usage: python stt.py audiofile")
    sys.exit(1)

audio_path = Path(sys.argv[1])

deepgram = DeepgramClient(api_key=API_KEY)

with open(audio_path, "rb") as f:
    audio_data = f.read()

response = deepgram.listen.v1.media.transcribe_file(
    request=audio_data,
    model="nova-3",
    smart_format=True,
    punctuate=True,
    diarize=True
)

result = response.model_dump(mode="json")

transcript = result["results"]["channels"][0]["alternatives"][0]["transcript"]

print("\nTRANSCRIPT\n")
print(transcript)

txt_file = audio_path.with_suffix(".txt")
txt_file.write_text(transcript)

json_file = audio_path.with_suffix(".json")
json_file.write_text(json.dumps(result, indent=2))

print(f"\nSaved transcript: {txt_file}")
print(f"Saved JSON: {json_file}")
