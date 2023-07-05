import numpy as np
import pandas as pd
from decouple import config
from sqlalchemy import create_engine
from pandasql import sqldf

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


def get_data_from_report1():
    uri = DATABASEURL.format(
        USER=config('USERDB'),
        PASSWORD=config('PASSBD'),
        DB=config('DB')
    )

    engine = create_engine(uri, echo=False)

    with open('db/query1.sql', 'r') as f:
        query = f.read()

    return pd.read_sql(query, con=engine)

def get_data_from_report2():
    uri = DATABASEURL.format(
        USER=config('USERDB'),
        PASSWORD=config('PASSBD'),
        DB=config('DB')
    )

    engine = create_engine(uri, echo=False)

    with open('db/query2.sql', 'r') as f:
        query = f.read()

    return pd.read_sql(query, con=engine)

def export_to_csv(data: pd.DataFrame, filename: str):
    return data.to_csv(filename, index=False)






