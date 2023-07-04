import requests

from const import BASEURL


def get_qoute(coin) -> list[dict]:

    response = requests.get(BASEURL.format(coin=coin))
    response.raise_for_status()

    return [x | {'coinId': coin} for x in response.json()]
