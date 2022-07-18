import logging
from datetime import datetime, timedelta

import requests

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "ded11a1cbd164242b6bb28c51f1dad5f"
API_VERSION = "2.0"

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
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }

    # we want to retrieve all previous requests from the last 30 days
    from_datetime = datetime.now() - timedelta(days=30)
    from_datetime_tz_aware = from_datetime.astimezone()
    payload = {
        "timestamp": from_datetime_tz_aware.isoformat(),
        "result_count": 1,
    }

    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == "__main__":
    json_data = invoke_searches_historic()
    logger.info(f"Found {json_data.get('count', 0)} results.")
