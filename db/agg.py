from datetime import timedelta

import numpy as np
import pandas as pd
from decouple import config
from sqlalchemy import create_engine

from const import DATABASEURL


def agg_data():
    uri = DATABASEURL.format(
        USER=config('USERDB'),
        PASSWORD=config('PASSBD'),
        DB=config('DB')
    )

    engine = create_engine(uri, echo=False)

    data = pd.read_sql_table('coin_price', uri, index_col=None). \
        drop(columns=['icon', 'name', 'symbol', 'rank', 'volume', 'websiteUrl', 'insert_date'])
    data['event_time'] = pd.to_datetime(data['event_time'])

    data_agg = data.groupby('id'). \
        rolling(window=timedelta(seconds=5), on='event_time'). \
        agg(
            {"price": [np.max, np.min, np.mean, np.count_nonzero]}
        ).\
        reset_index(level=[0,1])
    data_agg.columns = ['_'.join(col) for col in data_agg.columns.values]
    data_agg = data_agg.rename(columns={'id_': 'name', 'event_time_': 'event_time'})

    data_agg.to_sql('coin_agg', con=engine, if_exists='replace', index=False)


agg_data()