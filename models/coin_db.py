from __future__ import annotations

import faust


class CoinDB(faust.Record, serializer='json'):
    price: float
    exchange: str
    pair: str
    pairPrice: float
    volume: int
    event_time: str


