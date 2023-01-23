import logging

import requests

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "2.0"

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
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }
    params = {
        "name": "juan",
        "country_residence": "FR",
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == "__main__":
    json_data = invoke_search()
    logger.info(f"Found {json_data.get('count', 0)} results.")
