import random
from datetime import datetime

import faust

SYMBOLLIST = [
    "MSFT",
    "AMZN",
    "SNOW",
    "NVDA",
    "GOOG",
    "AAPL",
]

START_PRICE = 50


class Stock(faust.Record):
    stock_symbol: str
    stock_price: float
    timestamp: datetime

class StockSink(faust.Record):
    stock_symbol: str
    stock_price: float
    timestamp: datetime
    timestamp_sink: datetime

app = faust.App('hello-app', broker='kafka://localhost')
stock_in = app.topic('stock_in', value_type=Stock, partitions=3)
stock_sink = app.topic('stock_sink', value_type=Stock, partitions=3)
db = app.topic('db', value_type=Stock, partitions=3)


def select_stock() -> str:
    return random.choice(SYMBOLLIST)


def generate_stock() -> int:
    return random.randint(-5, 5)

def consume_stock(stock: Stock) -> str:
    return f'Stock: {stock.stock_symbol}, Price: USD {stock.stock_price}'


# Topic to write stock price
@app.timer(interval=0.5)
async def stock_price() -> None:
    """Send a message to the price_in topic."""
    stock_price = START_PRICE + generate_stock()
    stock_name = select_stock()
    time = datetime.now()
    data = Stock(stock_symbol=stock_name, stock_price=stock_price, timestamp=time)
    await stock_in.send(value=data)

# Sink data from one topic do other
@app.agent(stock_in)
async def process_messages(messages):
    async for message in messages:
        print(consume_stock(message))
        db = StockSink(
            stock_symbol=message.stock_symbol,
            stock_price=message.stock_price,
            timestamp=message.timestamp,
            timestamp_sink=datetime.now()
        )
        await stock_sink.send(value=db)


if __name__ == '__main__':
    app.main()