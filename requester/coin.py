import requests

from const import BASEURL


def get_qoute(coin) -> dict:

    response = requests.get(BASEURL.format(coin=coin))
    response.raise_for_status()

    return response.json()

get_qoute('bitcoin')
get_qoute('ethereum')
get_qoute('cardano')