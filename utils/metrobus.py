import os
import json
import boto3
import logging
from dotenv import load_dotenv
from utils.cdmx_api import fetch_records

load_dotenv()


def current_status():
    data = fetch_records('prueba_fetchdata_metrobus', 1000)

    nrows = data.get('nhits')
    logging.info(f'Fetched {nrows} rows for the current status data')
    timestamp = data.get('records')[0].get('record_timestamp')
    date = timestamp[:10]
    s3_path = f'api/metrobus-current-location/{date}/{timestamp}'
    s3_data = json.dumps(data)

    try:
        s3 = boto3.client('s3')
        s3.put_object(Body=s3_data, Bucket=os.getenv('BUCKET_NAME'), Key=s3_path)
        logging.info(f'Saved {timestamp} file to s3 bucket')
    except Exception as e:
        logging.error(f'Failed to save {timestamp} to s3 bucket with exception:')
        logging.error(e)
        return False
    
    return True
