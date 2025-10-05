import os
import uuid
from dotenv import load_dotenv
from fpdf import FPDF
import google.generativeai as genai


class MeetingMinutesGenerator:
    """
    Handles audio transcription and meeting minutes generation using Google Gemini API.
    """

    def __init__(self):
        # Load environment variables from .env
        load_dotenv()
        self.google_api_key = os.getenv("GOOGLE_API_KEY")

        if not self.google_api_key:
            raise ValueError("Google API Key not set in .env file")

        # Configure Gemini
        genai.configure(api_key=self.google_api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def transcribe_audio(self, audio_path: str, progress=None) -> str:
        """
        Transcribe MP3 audio using Google Gemini (mocked behavior — Gemini doesn’t yet support direct audio transcription).
        You can replace this with Google Speech-to-Text API for real transcription if desired.
        """
        if progress:
            progress(0.3, desc="Transcribing audio...")

        try:
            # Placeholder: simulate audio transcription
            transcription = (
                "This is a simulated transcription. Replace this with actual transcription logic."
            )
            return transcription
        except Exception as e:
            return f"Error during transcription: {str(e)}"

    def generate_minutes(self, transcription: str, progress=None) -> str:
        """
        Generate professional meeting minutes from transcription using Google Gemini.
        """
        if progress:
            progress(0.6, desc="Generating meeting minutes...")

        prompt = f"""
        You are a professional meeting minutes writer.
        Generate meeting minutes in markdown format with a refined, formal style.
        Include:
        - Summary (attendees, date, location)
        - Discussion Points
        - Key Takeaways
        - Action Items with Owners

        Transcript:
        {transcription}
        """

        try:
            response = self.model.generate_content(prompt)
            minutes = response.text
        except Exception as e:
            minutes = f"Error generating minutes: {str(e)}"

        if progress:
            progress(0.9, desc="Finalizing minutes...")

        return minutes

    def generate_pdf(self, minutes_text: str) -> str:
        """
        Generate a PDF file from meeting minutes.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in minutes_text.split("\n"):
            pdf.multi_cell(0, 10, txt=line)
        pdf_file = f"meeting_minutes_{uuid.uuid4().hex}.pdf"
        pdf.output(pdf_file)
        return pdf_file

    def process_upload(self, audio_file: str, progress=None):
        """
        Process uploaded MP3: transcribe, generate minutes, and create PDF.
        Yields (minutes, pdf_file) with intermediate progress updates.
        """
        if not audio_file:
            yield ("Please upload an audio file.", None)
            return

        if not str(audio_file).lower().endswith(".mp3"):
            yield ("Please upload an MP3 file.", None)
            return

        yield ("Starting process...", None)
        if progress:
            progress(0.1, desc="Starting process...")

        transcription = self.transcribe_audio(audio_file, progress=progress)
        if isinstance(transcription, str) and transcription.startswith("Error"):
            yield (transcription, None)
            return

        yield ("Audio transcribed. Generating meeting minutes...", None)
        minutes = self.generate_minutes(transcription, progress=progress)

        pdf_file = self.generate_pdf(minutes)
        if progress:
            progress(1.0, desc="Process complete!")
        yield (minutes, pdf_file)
