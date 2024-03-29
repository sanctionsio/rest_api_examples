import logging

import requests

HOSTNAME = "api.sanctions.io"
BEARER_TOKEN = "12345678-12AF-12aF-12aF-1234567890aF"
API_VERSION = "2.1"

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def invoke_export():
    """
    Example showing how to call the /exporter endpoint.

    :return: bytes
    """
    url = f"https://{HOSTNAME}/exporter/"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Accept": f"application/json; version={API_VERSION}",
    }

    response = requests.get(url, headers=headers)

    return response.content


if __name__ == "__main__":
    file_content = invoke_export()
    file_name = "export.csv"
    with open(file_name, "wb") as export_file:
        export_file.write(file_content)
    logger.info("file successfully downloaded %s", file_name)
