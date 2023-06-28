SYMBOLLIST = [
    "MSFT",
    "AMZN",
    "SNOW",
    "NVDA",
    "GOOG",
    "AAPL",
]

SYMBOLS = {"symbol":','.join(SYMBOLLIST)}

BASEURL = 'https://api.coinstats.app/public/v1/coins?skip=0&limit=10'

DATABASEURL = 'postgresql://{USER}:{PASSWORD}@localhost:5433/{DB}'
