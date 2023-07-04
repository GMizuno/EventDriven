from __future__ import annotations

import faust


class CoinDB(faust.Record, serializer='json'):
    price: float
    exchange: str
    coinId: str
    volume: int
    event_time: str


