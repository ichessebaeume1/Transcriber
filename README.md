# Transcriber
This program extracts audio from a video file, transcribes the audio using OpenAI's Whisper model, and saves the transcription into a PDF file.

## Installation

### Step 1: Install Python

1. Download Python from the official website: [Python Downloads](https://www.python.org/downloads/release/python-3124/)
2. Follow the installation instructions for your operating system.
3. Check the "Add Python to PATH" box during the installation.

### Step 2: Install Required Libraries

1. Download this repo as a .zip file and extract it.
2. Go into the folder you just extracted, right-click the empty space, and click on: "Open in Terminal"
3. Run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

### Step 3: Run the program
1. Run the following command to start the program:
```bash
python3 transcriber.py
```
2. Put in the path to the video you want to transcribe and hit enter.
3. Wait.

Note: If you upload a long video, the AI takes some time to transcribe it.
