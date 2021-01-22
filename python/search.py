import logging

import requests
from requests import HTTPError

HOSTNAME = "sandbox.sanctions.io"
BEARER_TOKEN = "Bearer ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "1.0"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_search():
    """
    Example showing how to call the /search endpoint.
    :return: dict
    """
    url = f"https://{HOSTNAME}/search"
    headers = {
        "Authorization": BEARER_TOKEN,
        "Accept": f"application/json; version={API_VERSION}"
    }
    params = {
        "name": "juan",
        "countries": "FR"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except (HTTPError, Exception):
        logger.exception(f'GET {url} failed.')
        return {}
    else:
        return response.json()


if __name__ == "__main__":
    json_data = invoke_search()
    results = json_data.get('results', [])
    logger.info(f"Found {len(results)} results.")
