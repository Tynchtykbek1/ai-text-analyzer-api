from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Text Analyzer API is running"}