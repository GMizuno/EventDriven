from datetime import datetime

import faust

from const import COINSLIST
from db.agg import agg_data
from db.sink import sink_postgres
from models import Coin
from requester.coin import get_qoute

app = faust.App('coin-app', broker='kafka://localhost')
stock_in = app.topic('stock_in', value_type=Coin, partitions=3)
stock_sink = app.topic('stock_sink', value_type=Coin, partitions=3)


# Topic to write stock price
@app.timer(interval=5)
async def stock_price() -> None:
    """Consume stock price from one topic."""
    for coin in COINSLIST:
        results = get_qoute(coin)
        print('Get results from API')
        for result in results:
            result['event_time']= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            model_result = Coin(**result)
            await stock_sink.send(value=model_result)

@app.agent(stock_sink)
async def process_messages(messages):
    """Transform stock information to stock sink data"""
    async for message in messages:
        print('Sending message to postgres')
        sink_postgres(message.asdict())
        agg_data()


if __name__ == '__main__':
    app.main()
