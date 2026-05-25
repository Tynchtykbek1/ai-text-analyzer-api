# AI Text Analyzer API

This is a beginner AI Engineering backend project built with Python, FastAPI, and Gemini API.

The project analyzes text, returns structured text statistics, and can generate an AI summary using Gemini.

## Features

- Text analysis with Python
- FastAPI backend
- JSON API responses
- Gemini AI summary endpoint
- Environment variable setup with `.env`
- Interactive API documentation with Swagger UI
- Automated tests with `pytest`
- Mocked tests for AI endpoint
- Git version control

## Project Structure

```text
ai-text-analyzer-api/
├── app.py
├── ai_client.py
├── analyzer.py
├── schemas.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── tests/
    ├── conftest.py
    ├── test_analyzer.py
    └── test_api.py
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

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

A sample file is provided:

```text
.env.example
```

Important:

```text
.env is ignored by Git and must not be pushed to GitHub.
.env.example is safe to push because it does not contain a real API key.
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
Average word length: 6.11
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

## API Endpoints

### GET `/`

Health check endpoint.

Response:

```json
{
    "message": "AI Text Analyzer API is running"
}
```

---

### POST `/analyze`

Analyzes text and returns basic statistics.

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
    "average_word_length": 6.11
}
```

---

### POST `/summarize`

Generates a short AI summary using Gemini.

Request body:

```json
{
    "text": "AI engineering is not only about prompts. It requires backend skills, APIs, testing, deployment, security, and the ability to build reliable systems."
}
```

Example response:

```json
{
    "summary": "AI engineering requires more than writing prompts; it involves backend development, APIs, testing, deployment, security, and reliable system design."
}
```

## Validation

The API validates input text:

- Text cannot be empty
- Text cannot be longer than 5000 characters

If invalid input is sent, FastAPI returns a validation error.

## Error Handling

The `/summarize` endpoint includes basic error handling:

- Missing API key returns a server error
- Gemini service failure returns a controlled error response

Example error response:

```json
{
    "detail": "AI summary service is currently unavailable"
}
```

## Running Tests

Run all tests:

```bash
python -m pytest
```

Expected result:

```text
10 passed
```

The tests cover:

- Text analysis functions
- API home endpoint
- `/analyze` endpoint
- Input validation
- `/summarize` endpoint with mocked Gemini response
- Error handling for AI service failure

## Current Status

The project currently provides:

- Basic text analysis
- FastAPI backend
- Gemini-powered AI summary endpoint
- Input validation
- Error handling
- Automated tests

## Next Steps

- Add Docker support
- Add deployment instructions
- Add request logging
- Add better text preprocessing
- Add frontend or simple web interface
- Add more AI features such as sentiment analysis or keyword extraction