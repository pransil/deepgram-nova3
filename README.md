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
