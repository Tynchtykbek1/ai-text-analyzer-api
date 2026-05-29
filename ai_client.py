import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_MODEL = "gemini-2.5-flash"


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
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text


def extract_ai_keywords(text):
    client = get_gemini_client()

    prompt = f"""
Extract 5 important keywords or key phrases from the following text.

Text:
{text}

Return only the keywords, separated by commas.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    keywords_text = response.text
    keywords = [
        keyword.strip()
        for keyword in keywords_text.split(",")
        if keyword.strip()
    ]

    return keywords

def generate_ai_full_insight(text):
    client = get_gemini_client()

    prompt = f"""
Analyze the following text.

Text:
{text}

Return only valid JSON in this exact format:
{{
    "summary": "short clear summary here",
    "keywords": ["keyword 1", "keyword 2", "keyword 3", "keyword 4", "keyword 5"]
}}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    raw_text = response.text.strip()
    raw_text = raw_text.replace("```json", "").replace("```", "").strip()

    data = json.loads(raw_text)

    return {
        "summary": data["summary"],
        "keywords": data["keywords"],
    }