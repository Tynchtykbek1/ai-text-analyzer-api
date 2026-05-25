from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "AI Text Analyzer API is running"
    }


def test_analyze_endpoint():
    response = client.post(
        "/analyze",
        json={
            "text": "AI engineering requires Python, APIs, and clean project structure."
        },
    )

    data = response.json()

    assert response.status_code == 200
    assert data["text"] == "AI engineering requires Python, APIs, and clean project structure."
    assert data["word_count"] == 9
    assert data["character_count"] == 66
    assert data["sentence_count"] == 1
    assert data["average_word_length"] == 6.11


def test_analyze_endpoint_rejects_empty_text():
    response = client.post(
        "/analyze",
        json={
            "text": ""
        },
    )

    assert response.status_code == 422



def test_summarize_endpoint_with_mock(monkeypatch):
    def fake_generate_ai_summary(text):
        return "Mocked AI summary."

    monkeypatch.setattr("app.generate_ai_summary", fake_generate_ai_summary)

    response = client.post(
        "/summarize",
        json={
            "text": "AI engineering requires backend skills and testing."
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked AI summary."
    }


def test_summarize_endpoint_handles_ai_error(monkeypatch):
    def fake_generate_ai_summary(text):
        raise Exception("Gemini API error")

    monkeypatch.setattr("app.generate_ai_summary", fake_generate_ai_summary)

    response = client.post(
        "/summarize",
        json={
            "text": "AI engineering requires reliable error handling."
        },
    )

    assert response.status_code == 502
    assert response.json() == {
        "detail": "AI summary service is currently unavailable"
    }