import moviepy.editor as mp
import whisper
from fpdf import FPDF
import os


def extract_audio_from_video(video_path):
    # Load the video
    video = mp.VideoFileClip(video_path)
    # Extract audio
    audio_path = os.path.splitext(video_path)[0] + ".mp3"
    video.audio.write_audiofile(audio_path)
    return audio_path


def transcribe_audio(audio_path):
    # Load Whisper model
    print("Whisper AI - Loading Model...")
    model = whisper.load_model("base")
    # Transcribe audio
    print("Whisper AI - Transcribing Audio")
    result = model.transcribe(audio_path)
    print("Whisper AI - Done.")
    return result['text']


def save_transcription_as_pdf(transcription, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in transcription.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_path)


def transcribe_video(video_path):
    # Extract audio from video
    audio_path = extract_audio_from_video(video_path)
    # Transcribe audio
    transcription = transcribe_audio(audio_path)
    # Prepare PDF file path
    pdf_path = os.path.splitext(video_path)[0] + "_transcript.pdf"
    # Save transcription to PDF
    save_transcription_as_pdf(transcription, pdf_path)
    # Delete temp files
    print("Cleaning up...")
    os.remove(audio_path)
    return pdf_path


# Example usage
video_path = rf"{input('Video Path: ')}"
pdf_path = transcribe_video(video_path)
print("Transcription saved to: ", pdf_path)
