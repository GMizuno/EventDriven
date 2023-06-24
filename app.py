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


app = faust.App('hello-app', broker='kafka://localhost')
stock_in = app.topic('stock_in', key_type=Stock, value_type=Stock)
db = app.topic('db', key_type=Stock, value_type=Stock)


def select_stock() -> str:
    return random.choice(SYMBOLLIST)


def generate_stock() -> int:
    return random.randint(-5, 5)

def consume_stock(stock: Stock) -> str:
    return f'Stock: {stock.stock_symbol}, Price: {stock.stock_price}'


# Topic to write stock price
@app.timer(interval=5.0)
async def stock_price() -> None:
    """Send a message to the price_in topic."""
    stock_price = START_PRICE + generate_stock()
    stock_name = select_stock()
    time = datetime.now()
    data = Stock(stock_symbol=stock_name, stock_price=stock_price, timestamp=time)
    await stock_in.send(value=data)

@app.agent(stock_in)
async def stock_in(stock: faust.Topic) -> None:
    """Consume the stock price."""
    result = stock
    print(result)


if __name__ == '__main__':
    app.main()