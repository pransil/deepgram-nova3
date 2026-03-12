import sys
import json
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python show_transcript.py <json_file>")
    sys.exit(1)

data = json.loads(Path(sys.argv[1]).read_text())
words = data["results"]["channels"][0]["alternatives"][0]["words"]

def fmt_time(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"

# Group consecutive words by speaker into paragraphs
paragraphs = []
current_speaker = None
current_words = []
current_start = 0.0

for w in words:
    speaker = w.get("speaker", 0)
    if speaker != current_speaker:
        if current_words:
            paragraphs.append((current_speaker, current_start, " ".join(current_words)))
        current_speaker = speaker
        current_words = [w["punctuated_word"]]
        current_start = w["start"]
    else:
        current_words.append(w["punctuated_word"])

if current_words:
    paragraphs.append((current_speaker, current_start, " ".join(current_words)))

for speaker, start, text in paragraphs:
    print(f"[Speaker {speaker}] {fmt_time(start)}")
    print(text)
    print()
