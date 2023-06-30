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
        drop(columns=['icon', 'name', 'symbol', 'rank', 'volume', 'websiteUrl', 'event_time', 'insert_date'])

    data_agg = data.groupby('id').agg(
        min_price=('price', np.min),
        max_price=('price', np.max),
        avg_price=('price', np.mean),
        count=('price', np.count_nonzero)
    ).reset_index().\
        rename(columns={'id': 'name'})

    data_agg.to_sql('coin_agg', con=engine, if_exists='replace', index=False)


