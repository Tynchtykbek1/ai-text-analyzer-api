from fastapi import FastAPI

from ai_client import generate_ai_summary
from analyzer import analyze_text
from schemas import SummaryResponse, TextAnalysisResponse, TextRequest


app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}


@app.post("/analyze", response_model=TextAnalysisResponse)
def analyze(request: TextRequest):
    result = analyze_text(request.text)
    return result


@app.post("/summarize", response_model=SummaryResponse)
def summarize(request: TextRequest):
    summary = generate_ai_summary(request.text)
    return {"summary": summary}