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

    data = pd.read_sql_table('coin_price', uri, index_col=None).drop(columns=['insert_date'])
    data['event_time'] = pd.to_datetime(data['event_time'])

    data_agg = data.groupby([pd.Grouper(key='event_time', freq='5S'), 'exchange', 'pair']).agg(
        {"price": [np.max, np.min, np.mean, np.count_nonzero]}
    ).reset_index()

    data_agg.sort_values(by=['event_time', 'exchange', 'pair'], inplace=True)

    data_agg.to_sql('coin_agg', con=engine, if_exists='replace', index=False)

df_time = pd.DataFrame({'B': [0, 1, 2, 5, np.nan, 4],
                        'time': [pd.Timestamp('20130101 09:00:01'),
                                 pd.Timestamp('20130101 09:00:02'),
                                 pd.Timestamp('20130101 09:00:03'),
                                 pd.Timestamp('20130101 09:00:04'),
                                 pd.Timestamp('20130101 09:00:07'),
                                 pd.Timestamp('20130101 09:00:09')]},
                       )
df_time.rolling('2s', center=True, on='time', closed='left').sum()

df_time.resample('5S', on='time').B.sum()
dir(data.resample('5S', on='event_time'))
