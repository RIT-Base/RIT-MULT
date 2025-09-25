# This serve as main code + reference for this project.
# Single endpoint + tool.

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#Add more tools import below:

from tools import base64_converter, reverse_text, word_counter

#App Instance
app = FastAPI(
    title="RIT-Mult-Tools",
    description="API Gateway for various simple tools",
    version="0.1"
)

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500/index.html" # for local testing with Live Server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Plug & Play Section
app.include_router(base64_converter.router, prefix="/crypto_tools", tags=["Base64 Converter"])
app.include_router(reverse_text.router, prefix="/text_tools", tags=["Text Reversal"])
app.include_router(word_counter.router, prefix="/text_tools", tags=["Word Counter"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multi-Utility Tool API! Go to /docs to see the available tools."}