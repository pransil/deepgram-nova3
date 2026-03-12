# Deepgram Nova-3 STT Test

A simple test of [Deepgram's Nova-3](https://deepgram.com) speech-to-text model using two audio files:

- **jfk.m4a** — JFK's "Ask not what your country can do for you" excerpt
- **wildfires.mp3** — Wildfire news audio clip

## Setup

```bash
python -m venv deepgram-env
source deepgram-env/bin/activate
pip install deepgram-sdk
```

Set your Deepgram API key:

```bash
export DEEPGRAM_API_KEY=your_api_key_here
```

## Usage

```bash
python stt.py jfk.m4a
python stt.py wildfires.mp3
```

Each run prints the transcript to stdout and saves two files alongside the audio:
- `<filename>.txt` — plain transcript
- `<filename>.json` — full Deepgram response (includes word timings, diarization, confidence scores, etc.)

## Visualizing the transcript with speaker diarization

The raw `.json` output contains rich per-word metadata — including which speaker said each word and when. `show_transcript.py` makes this human-readable by grouping words into paragraphs by speaker, with timestamps.

This is useful when there are multiple speakers (e.g. an interview or a meeting), since the plain `.txt` file is one undifferentiated block of text. The diarized view makes it immediately clear who said what and at what point in the audio.

```bash
python show_transcript.py wildfires.json
```

Example output:

```
[Speaker 0] 00:00
Smoke from hundreds of wildfires in Canada is triggering air quality alerts throughout The US...

[Speaker 1] 01:45
Good morning. So what is it about the conditions right now that have caused this round of wildfires...
```

Works with the JSON output from any `stt.py` run.
