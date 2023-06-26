from typing import Optional

from faust import Record


class Symbol(Record, serializer='json'):
    id: str
    icon: str
    name: str
    symbol: str
    rank: int
    price: float
    priceBtc: int
    volume: float
    marketCap: float
    availableSupply: int
    totalSupply: int
    priceChange1h: float
    priceChange1d: float
    priceChange1w: float
    websiteUrl: str
    twitterUrl: str
    exp: list[str]
    contractAddress: str = None
    decimals: int = None
    redditUrl: str = None


class SymbolSink(Record, serializer='json'):
    id: str
    icon: str
    name: str
    symbol: str
    rank: int
    price: float
    volume: float
    websiteUrl: str