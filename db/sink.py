import pandas as pd
from sqlalchemy import create_engine
from decouple import config
from sqlalchemy import text

from const import DATABASEURL


def sink_postgres(data: dict):
    data = pd.DataFrame(data, index=[0])

    engine = create_engine(
        DATABASEURL.format(USER=config('USERDB'), PASSWORD=config('PASSBD'), DB=config('DB')),
        echo=False
    )

engine = create_engine(
    DATABASEURL.format(USER=config('USERDB'), PASSWORD=config('PASSBD'), DB=config('DB')),
    echo=False
)



with engine.connect() as conn:
    conn.execute(text("SHOW TABLES")).fetchall()
