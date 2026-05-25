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