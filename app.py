from fastapi import FastAPI
from pydantic import BaseModel

from analyzer import analyze_text


app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}


@app.post("/analyze")
def analyze(request: TextRequest):
    result = analyze_text(request.text)
    return result