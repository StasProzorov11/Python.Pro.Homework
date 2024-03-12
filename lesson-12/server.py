import json
import random
import string

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


def create_random_string(size: int) -> str:
    return "".join([random.choice(string.ascii_letters) for _ in range(size)])


@app.post("/generate-article")
async def get_information():
    data = {
        "title": create_random_string(10),
        "description": create_random_string(20),
    }

    with open("data.json", "w") as file:
        json.dump(data, file)

    return data


@app.post("/fetch-market")
async def get_current_market_state(from_currency: str, to_currency: str):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey=V2V43QAQ8RILGBOW"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    with open("market_data.json", "w") as file:
        json.dump(data, file)

    return data
