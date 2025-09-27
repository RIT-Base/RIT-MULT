from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Input(BaseModel):
    data: str

@router.post("/reverse")
async def reverse_text(payload: Input):
    return {"result": payload.text[::-1]}
