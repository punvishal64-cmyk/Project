import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def categorize_activity(transcript: str) -> dict:
    prompt = f"""
You are an activity categorization assistant.

Return ONLY valid JSON.

Format:
{{
    "category": "...",
    "task": "..."
}}

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    try:
        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)

    except json.JSONDecodeError:
        return {
            "category": "Unknown",
            "task": transcript,
            "error": "LLM returned invalid JSON"
        }