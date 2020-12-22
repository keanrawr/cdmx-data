import logging
import requests
from time import sleep


def fetch_records(dataset, rows, **kwargs):
    url = 'https://datos.cdmx.gob.mx/api/records/1.0/search/'
    params = {
        'dataset': dataset,
        'rows': rows,
        **kwargs
    }

    finished = False
    while not finished:
        res = requests.get(url, params=params)
        if res.status_code == 200:
            finished = True
            logging.info(f'Request successful for dataset: {dataset}')
        else:
            logging.warning(f'Got status {res.status_code} for dataset: {dataset}. Retrying in 1 second')
            sleep(1)

    return res.json()

