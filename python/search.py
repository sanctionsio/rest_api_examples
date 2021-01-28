import logging

import requests

HOSTNAME = 'sandbox.sanctions.io'
BEARER_TOKEN = 'ded11a1cbd164242b6bb28c51f1dad5f'
API_VERSION = '1.0'

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_search():
    """
    Example showing how to call the /search endpoint.
    :return: dict
    """
    url = f'https://{HOSTNAME}/search'
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
        'Accept': f'application/json; version={API_VERSION}'
    }
    params = {
        'name': 'juan',
        'countries': 'FR',
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == '__main__':
    json_data = invoke_search()
    logger.info(json_data)
    results = json_data.get('results', [])
    logger.info(f'Found {len(results)} results.')
