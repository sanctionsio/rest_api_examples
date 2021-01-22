import logging
from datetime import datetime

import requests
import urllib.parse

from requests import HTTPError

HOSTNAME = "sandbox.sanctions.io"
BEARER_TOKEN = "Bearer ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "1.0"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_searches_historic():
    """
    Example showing how to call the /searches/historic endpoint.
    :return: dict
    """
    url = f"https://{HOSTNAME}/searches/historic"
    headers = {
        "Authorization": BEARER_TOKEN,
        "Accept": f"application/json; version={API_VERSION}"
    }

    current_datetime = datetime.now()
    current_zoned_datetime = current_datetime.astimezone()
    payload = {
        "timestamp": current_zoned_datetime.strftime('%Y-%m-%dT%H-%M-%S%z'),
        "result_count": 10
    }
    params = urllib.parse.urlencode(payload)
    params = params.replace('&', '%26')
    params = params.replace('=', '%3D')
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except (HTTPError, Exception):
        logger.exception(f'GET {url} failed.')
        return {}
    else:
        return response.json()


if __name__ == "__main__":
    json_data = invoke_searches_historic()
    results = json_data.get('results', [])
    logger.info(f"Found {len(results)} results.")
