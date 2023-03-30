import logging

import requests
from requests import HTTPError

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "12345678-12AF-12aF-12aF-1234567890aF"
API_VERSION = "2.1"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_programs():
    """
    Example showing how to call the /programs endpoint.
    :return: dict
    """
    url = f"https://{HOSTNAME}/programs"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }

    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == "__main__":
    json_data = invoke_programs()
    logger.info(f"Found {json_data.get('count', 0)} results.")
    names = [result.get("short_name") for result in json_data.get("results", [])]
    logger.info(f"Programs found: {', '.join(names)}")
