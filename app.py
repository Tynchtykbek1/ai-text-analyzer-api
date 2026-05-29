import logging
import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse

from ai_client import generate_ai_summary
from analyzer import analyze_text
from logger_config import configure_logging
from schemas import (
    FullAnalysisResponse,
    SummaryResponse,
    TextAnalysisResponse,
    TextRequest,
)


configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = round(time.time() - start_time, 4)

    logger.info(
        "%s %s - %s - %ss",
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ai-text-analyzer-api"
    }

@app.get("/ui")
def ui():
    return FileResponse("frontend/index.html")


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
    

@app.post("/full-analysis", response_model=FullAnalysisResponse)
def full_analysis(request: TextRequest):
    analysis = analyze_text(request.text)

    try:
        summary = generate_ai_summary(request.text)
        return {
            "analysis": analysis,
            "summary": summary,
        }
    except ValueError as error:
        raise HTTPException(status_code=500, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI summary service is currently unavailable"
        )