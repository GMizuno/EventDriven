from __future__ import annotations

import faust


class Coin(faust.Record, serializer='json'):
    price: float
    exchange: str
    coinId: str
    pair: str
    pairPrice: float
    event_time: str
    volume: int = None
