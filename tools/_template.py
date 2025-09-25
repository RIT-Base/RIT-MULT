"""
Template Tool
-------------

Gunakan file ini sebagai template ketika membuat tool baru.
Cukup copy file ini, rename sesuai nama tool, lalu isi logikanya.
"""

from fastapi import APIRouter
from pydantic import BaseModel

# Router untuk tool ini
router = APIRouter()

# Contoh model input (hapus/ubah sesuai kebutuhan)
class ExampleInput(BaseModel):
    text: str

# Contoh endpoint (hapus/ubah sesuai kebutuhan)
@router.post("/example")
async def example_endpoint(payload: ExampleInput):
    """
    Deskripsi singkat tool.
    Ganti dengan penjelasan apa yang dilakukan oleh tool ini.
    """
    return {"message": f"Input kamu adalah: {payload.text}"}
