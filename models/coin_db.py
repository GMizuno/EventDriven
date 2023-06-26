from pydantic import BaseModel


class CoinDb(BaseModel):
    id: str
    icon: str
    name: str
    symbol: str
    rank: int
    price: float
    volume: float
    websiteUrl: str

import json

with open('sample_data.json') as f:
    coins = json.load(f)

data = CoinDb(**coins)