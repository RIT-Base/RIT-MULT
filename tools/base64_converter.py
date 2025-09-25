from fastapi import APIRouter
from pydantic import BaseModel
import base64

#Router Instance
router = APIRouter()

#For autocompletions.
class StringPayload(BaseModel):
    data: str

# Define the API endpoint, this is where your code and logics goes :

@router.post("/encode_base64")
async def encode_base64(payload: StringPayload):
    """
    Encodes a given string into a Base64 string.
    """
    encoded_bytes = base64.b64encode(payload.data.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return {"original_string": payload.data, "base64_string": encoded_string}

@router.post("/decode_base64")
async def decode_base64(payload: StringPayload):
    """
    Decodes a Base64 string back to its original string.
    """
    try:
        decoded_bytes = base64.b64decode(payload.data)
        decoded_string = decoded_bytes.decode('utf-8')
        return {"original_base64": payload.data, "decoded_string": decoded_string}
    except Exception as e:
        return {"error": "Invalid Base64 string", "details": str(e)}