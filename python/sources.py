import logging

import requests

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "12345678-12AF-12aF-12aF-1234567890aF"
API_VERSION = "2.1"

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
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }

    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == "__main__":
    json_data = invoke_sources()
    logger.info(f"Found {json_data.get('count', 0)} results.")
    names = [result.get("short_name") for result in json_data.get("results", [])]
    logger.info(f"Sources found: {', '.join(names)}")
