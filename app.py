from fastapi import FastAPI
from pydantic import BaseModel, Field

from analyzer import analyze_text


app = FastAPI()


class TextRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=5000,
        description="Text that will be analyzed"
    )


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}


@app.post("/analyze")
def analyze(request: TextRequest):
    result = analyze_text(request.text)
    return result