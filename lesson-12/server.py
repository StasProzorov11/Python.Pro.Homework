import json
import random
import string
import time

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

cached_data = {"data": None, "timestamp": 0}


def create_random_string(size: int) -> str:
    return "".join([random.choice(string.ascii_letters) for _ in range(size)])


@app.post("/fetch-market")
async def get_current_market_state(from_currency: str, to_currency: str):
    current_time = time.time()

    if current_time - cached_data["timestamp"] < 10:
        return cached_data["data"]

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey=V2V43QAQ8RILGBOW"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    cached_data["data"] = data
    cached_data["timestamp"] = current_time

    with open("market_data.json", "w") as file:
        json.dump(data, file)

    return data
