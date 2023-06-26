import requests

from const import BASEURL


def get_qoute() -> dict:

    response = requests.get(BASEURL)
    response.raise_for_status()

    return response.json()

