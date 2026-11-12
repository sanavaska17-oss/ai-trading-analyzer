import os
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Trading Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "online",
        "mode": "demo",
        "message": "Server is running. Market data is not connected yet."
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/signal")
def signal():
    return {
        "pair": "EUR/USD",
        "signal": "WAIT",
        "reason": "Market data is not connected",
        "real_data": False,
        "timestamp": int(time.time())
    }
  
