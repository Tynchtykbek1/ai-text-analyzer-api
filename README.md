# AI Text Analyzer API

AI Text Analyzer API is a beginner-friendly AI Engineering backend project built with **Python**, **FastAPI**, **Gemini API**, and **Docker**.

The project provides text statistics, AI-generated summaries, keyword extraction, a simple frontend UI, automated tests, and Docker support.

## Features

- Text analysis with Python
- FastAPI backend API
- Gemini-powered AI summary generation
- Gemini-powered keyword extraction
- Full analysis endpoint combining statistics, summary, and keywords
- Simple frontend UI
- Input validation with Pydantic
- Error handling for AI service failures
- Request logging
- Automated tests with pytest
- Mocked tests for AI endpoints
- Docker support
- Environment variable setup with `.env`

## Technologies Used

- Python
- FastAPI
- Pydantic
- Gemini API
- Uvicorn
- Pytest
- Docker
- HTML, CSS, JavaScript
- Git and GitHub

## Project Structure

```text
ai-text-analyzer-api/
├── app.py
├── ai_client.py
├── analyzer.py
├── schemas.py
├── logger_config.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env.example
├── .gitignore
├── README.md
├── frontend/
│   └── index.html
└── tests/
    ├── conftest.py
    ├── test_analyzer.py
    └── test_api.py
```

## Main Endpoints

### GET `/`

Basic home endpoint.

Response:

```json
{
    "message": "AI Text Analyzer API is running"
}
```

### GET `/health`

Health check endpoint for deployment readiness.

Response:

```json
{
    "status": "ok",
    "service": "ai-text-analyzer-api"
}
```

### GET `/ui`

Serves the frontend user interface.

Open in browser:

```text
http://127.0.0.1:8000/ui
```

### POST `/analyze`

Returns basic text statistics.

Request:

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

### POST `/summarize`

Generates an AI summary using Gemini.

Request:

```json
{
    "text": "AI engineering requires backend skills, API integration, testing, Docker, deployment, and security."
}
```

Example response:

```json
{
    "summary": "AI engineering requires more than prompt writing; it involves backend development, API integration, testing, Docker, deployment, and security."
}
```

### POST `/keywords`

Extracts important keywords or key phrases using Gemini.

Request:

```json
{
    "text": "AI engineering requires backend development, API integration, testing, Docker, deployment, and security."
}
```

Example response:

```json
{
    "keywords": [
        "AI engineering",
        "backend development",
        "API integration",
        "testing",
        "Docker"
    ]
}
```

### POST `/full-analysis`

Returns text statistics, AI summary, and keywords in one response.

Request:

```json
{
    "text": "AI engineering is not only about writing prompts. It requires backend development, APIs, testing, Docker, deployment, security, and reliable systems."
}
```

Example response:

```json
{
    "analysis": {
        "text": "AI engineering is not only about writing prompts. It requires backend development, APIs, testing, Docker, deployment, security, and reliable systems.",
        "word_count": 18,
        "character_count": 149,
        "sentence_count": 2,
        "average_word_length": 7.0
    },
    "summary": "AI engineering requires more than prompts; it also needs backend development, APIs, testing, Docker, deployment, security, and reliable system design.",
    "keywords": [
        "AI engineering",
        "backend development",
        "APIs",
        "testing",
        "Docker"
    ]
}
```

## Input Validation

The API validates input text:

- Text cannot be empty
- Text cannot be longer than 5000 characters

Invalid input returns a FastAPI validation error.

## Error Handling

AI endpoints include error handling.

If Gemini is unavailable or returns an error, the API returns a controlled error response instead of crashing.

Example:

```json
{
    "detail": "AI full analysis service is currently unavailable"
}
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

A safe example file is included:

```text
.env.example
```

Important:

```text
.env contains the real API key and must never be pushed to GitHub.
.env.example is safe to push because it does not contain real secrets.
```

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Open the frontend:

```text
http://127.0.0.1:8000/ui
```

Open Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker

Make sure Docker Desktop is installed and running.

Build the Docker image:

```bash
docker build -t ai-text-analyzer-api .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 ai-text-analyzer-api
```

Open the app:

```text
http://127.0.0.1:8000/ui
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

Explanation:

```text
--env-file .env passes the Gemini API key into the container.
-p 8000:8000 maps port 8000 on your computer to port 8000 inside the container.
```

## Run Tests

Run all tests:

```bash
python -m pytest
```

Expected result:

```text
15 passed
```

The tests cover:

- Text analysis functions
- Home endpoint
- Health endpoint
- Analyze endpoint
- Input validation
- Summary endpoint with mocked Gemini response
- Keyword extraction endpoint with mocked Gemini response
- Full analysis endpoint with mocked Gemini response
- Error handling for AI service failures

## What This Project Demonstrates

This project demonstrates core AI Engineering skills:

- Building backend APIs
- Structuring a Python project
- Using AI APIs safely
- Managing environment variables
- Handling external API errors
- Writing automated tests
- Mocking AI services in tests
- Creating a simple frontend
- Running the application with Docker
- Keeping a clean Git history

## Current Status

The project is a complete beginner AI Engineering mini-project.

It includes:

- Backend API
- AI integration
- Frontend UI
- Testing
- Docker support
- Documentation

## Future Improvements

Possible next steps:

- Deploy to Render, Railway, or Fly.io
- Add authentication
- Add rate limiting
- Add persistent storage with PostgreSQL
- Add request history
- Add more advanced text analysis
- Add better frontend design
- Add CI/CD with GitHub Actions