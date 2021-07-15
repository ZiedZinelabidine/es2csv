import datetime
import logging
import requests
import json
from azure.storage.blob import BlockBlobService 


import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
 
    with open('/tmp/data.json', 'w') as f:
     r = requests.get('http://20.199.88.66:9200/shakespeare/_doc/44Uas3gBHTtB8ajuaNyg/_source')
    
     f.write(json.dumps(r.json(), sort_keys=True))
    
    block_blob_service = BlockBlobService(account_name='datasetspowerbi',
      account_key='BlBjKvzZgS7ctX1gTQlfbXqLiEAjuIKcF9cf1BwOojPgacEmOTEAAG4wXyYczFtCdRgJnOuXYbbtKagltTdUZQ==')
      
    block_blob_service.create_blob_from_path('data','data.json','/tmp/data.json')
    
  

