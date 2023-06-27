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


