import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as f:
        audio_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Transcribe the spoken audio exactly. Return ONLY the transcript.",
            types.Part.from_bytes(
                data=audio_bytes,
                mime_type="audio/webm",
            ),
        ],
    )

    return response.text.strip()