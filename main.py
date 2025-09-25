# This serve as main code + reference for this project.
# Single endpoint + tool.

from typing import Union
from fastapi import FastAPI

#Add more tools import below:

from tools import base64_converter, reverse_text

#App Instance
app = FastAPI(
    title="RIT-Mult-Tools",
    description="API Gateway for various simple tools",
    version="0.1"
)

#Plug & Play Section
app.include_router(base64_converter.router, prefix="/crypto_tools", tags=["Base64 Converter"])
app.include_router(reverse_text.router, prefix="/text_tools", tags=["Text Reversal"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multi-Utility Tool API! Go to /docs to see the available tools."}