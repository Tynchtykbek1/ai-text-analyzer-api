import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the .env file")

    return genai.Client(api_key=api_key)


def generate_ai_summary(text):
    client = get_gemini_client()

    prompt = f"""
Analyze the following text and provide a short, clear summary.

Text:
{text}

Return only the summary.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
    )

    return response.text