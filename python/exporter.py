import logging

import requests

HOSTNAME = 'sandbox.sanctions.io'
BEARER_TOKEN = 'ded11a1cbd164242b6bb28c51f1dad5f'
API_VERSION = '1.0'

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_export():
    """
    Example showing how to call the /exporter endpoint.

    :return: bytes
    """
    url = f'https://{HOSTNAME}/exporter/'
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
        'Accept': f'application/json; version={API_VERSION}'
    }

    response = requests.get(url, headers=headers)

    return response.content


if __name__ == '__main__':
    file_content = invoke_export()
    file_name = 'export.csv'
    with open(file_name, 'wb') as export_file:
        export_file.write(file_content)
    logger.info('file successfuly donwloaded %s', file_name)
