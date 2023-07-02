from datetime import datetime

import pandas as pd
from decouple import config
from sqlalchemy import create_engine

from const import DATABASEURL
from models import CoinDB


def sink_postgres(data: dict):
    engine = create_engine(
        DATABASEURL.format(USER=config('USERDB'), PASSWORD=config('PASSBD'), DB=config('DB')),
        echo=False
    )

    model = CoinDB(**data).asdict()
    data = pd.DataFrame(model, index=[0])
    data['insert_date'] = datetime.now()

    data.to_sql('coin_price', con=engine, if_exists='append', index=False)
    print('Data sinked to postgres')





