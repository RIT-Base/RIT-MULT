from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

class ExampleInput(BaseModel):
    data: str

# Contoh endpoint (hapus/ubah sesuai kebutuhan)
@router.post("/word_count")
async def example_endpoint(payload: ExampleInput):
    """
    Word Counter
    """
    text = payload.text.strip()
    
    words = text.split()
    word_count = len(words)
    char_count = len(text)

    return {
        "text": text,
        "word_count": word_count,
        "char_count": char_count,
    }

