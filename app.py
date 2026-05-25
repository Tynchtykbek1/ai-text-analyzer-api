from fastapi import FastAPI

from ai_client import generate_ai_summary
from analyzer import analyze_text
from schemas import SummaryResponse, TextAnalysisResponse, TextRequest
from fastapi import FastAPI, HTTPException

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
    try:
        summary = generate_ai_summary(request.text)
        return {"summary": summary}
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI summary service is currently unavailable"
        )