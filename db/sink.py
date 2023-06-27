from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine
from decouple import config

from const import DATABASEURL
from models.coin_db import CoinDb


def sink_postgres(data: dict):
    engine = create_engine(
        DATABASEURL.format(USER=config('USERDB'), PASSWORD=config('PASSBD'), DB=config('DB')),
        echo=False
    )

    model = CoinDb(**data).dict()
    data = pd.DataFrame(model, index=[0])
    data['insert_date'] = datetime.now()

    print(data.to_dict(orient='records'))
    data.to_sql('coin_price', con=engine, if_exists='append', index=False)
    print('Sinking data to postgres')





