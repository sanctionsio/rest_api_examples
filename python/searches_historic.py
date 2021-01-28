import logging
import urllib.parse
from datetime import datetime, timedelta

import requests

HOSTNAME = 'sandbox.sanctions.io'
BEARER_TOKEN = 'ded11a1cbd164242b6bb28c51f1dad5f'
API_VERSION = '1.0'

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_searches_historic():
    """
    Example showing how to call the /searches/historic endpoint.
    :return: dict
    """
    url = f'https://{HOSTNAME}/searches/historic'
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
        'Accept': f'application/json; version={API_VERSION}'
    }

    # we want to retrieve all previous requests from the las 30 days
    from_datetime = datetime.now() - timedelta(days=30)
    from_datetime_tz_aware = from_datetime.astimezone()
    payload = {
        'timestamp': from_datetime_tz_aware.strftime('%Y-%m-%dT%H-%M-%S%z'),
        'result_count': 10,
    }
    params = urllib.parse.urlencode(payload)
    params = params.replace('&', '%26')
    params = params.replace('=', '%3D')

    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == '__main__':
    json_data = invoke_searches_historic()
    logger.info(f"Found {json_data.get('count', 0)} results.")
