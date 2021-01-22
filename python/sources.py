import logging

import requests
from requests import HTTPError

HOSTNAME = "sandbox.sanctions.io"
BEARER_TOKEN = "Bearer ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "1.0"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_sources():
    """
    Example showing how to call the /sources endpoint.
    :return: dict
    """
    url = f"https://{HOSTNAME}/sources"
    headers = {
        "Authorization": BEARER_TOKEN,
        "Accept": f"application/json; version={API_VERSION}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except (HTTPError, Exception):
        logger.exception(f'GET {url} failed.')
        return {}
    else:
        return response.json()


if __name__ == "__main__":
    json_data = invoke_sources()
    results = json_data.get('results', [])
    names = [result.get('short_name') for result in results]
    logger.info(f"Sources found: {','.join(names)}")
