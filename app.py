from fastapi import FastAPI

from analyzer import analyze_text
from schemas import TextAnalysisResponse, TextRequest


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}


@app.post("/analyze", response_model=TextAnalysisResponse)
def analyze(request: TextRequest):
    result = analyze_text(request.text)
    return result