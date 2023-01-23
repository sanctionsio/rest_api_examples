import logging

import requests

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "2.1"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_plans():
    """
    Example showing how to call the /plans endpoint.
    :return: dict
    """
    url = f"https://{HOSTNAME}/plans"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }

    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == "__main__":
    json_data = invoke_plans()
    results = json_data.get("results", [])
    names = [result.get("plan_name") for result in results]
    logger.info(f"Plans found: {','.join(names)}")
