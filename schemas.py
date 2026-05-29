from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=5000,
        description="Text that will be analyzed"
    )


class TextAnalysisResponse(BaseModel):
    text: str
    word_count: int
    character_count: int
    sentence_count: int
    average_word_length: float

class SummaryResponse(BaseModel):
    summary: str

class FullAnalysisResponse(BaseModel):
    analysis: TextAnalysisResponse
    summary: str
    keywords: list[str]

class KeywordsResponse(BaseModel):
    keywords: list[str]