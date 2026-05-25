# AI Text Analyzer API

This is a beginner AI Engineering project built with Python and FastAPI.

The project analyzes text and returns structured information such as word count, character count, sentence count, and average word length.

## Features

- Text analysis with Python
- JSON output
- FastAPI backend
- Interactive API documentation with Swagger UI
- Git version control

## Project Structure

```text
ai-text-analyzer-api/
├── app.py
├── analyzer.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Install

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the CLI Version

```bash
python main.py
```

Example input:

```text
AI engineering requires Python, APIs, and clean project structure.
```

Example output:

```text
Analysis result:
Words: 9
Characters: 66
Sentences: 1
Average word length: 6.44
Result saved to analysis_result.json
```

## How to Run the API

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000/
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST `/analyze`

Request body:

```json
{
    "text": "AI engineering requires Python, APIs, and clean project structure."
}
```

Response:

```json
{
    "text": "AI engineering requires Python, APIs, and clean project structure.",
    "word_count": 9,
    "character_count": 66,
    "sentence_count": 1,
    "average_word_length": 6.44
}
```

## Current Status

The project currently provides basic text analysis through both a command-line interface and a FastAPI endpoint.

## Next Steps

- Add input validation
- Improve text cleaning
- Add AI API integration
- Add automated tests
- Add deployment instructions