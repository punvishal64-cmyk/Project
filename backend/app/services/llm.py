from ollama import chat
import json


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

    response = chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        return json.loads(response.message.content)

    except json.JSONDecodeError:
        return {
            "category": "Unknown",
            "task": transcript,
            "error": "LLM returned invalid JSON"
        }