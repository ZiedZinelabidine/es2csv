import logging
import pandas as pd

from azure.storage.blob import BlockBlobService 
from azure.storage.blob import ContentSettings  

import azure.functions as func


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
          
block_blob_service = BlockBlobService(account_name='datasetspowerbi',
account_key='BlBjKvzZgS7ctX1gTQlfbXqLiEAjuIKcF9cf1BwOojPgacEmOTEAAG4wXyYczFtCdRgJnOuXYbbtKagltTdUZQ==')

block_blob_service.get_blob_to_path('data', 'data.json', '/tmp/data.json')

df = pd.read_json ('/tmp/data.json',typ='series')
df.to_csv("/tmp/test.csv", sep='\t', encoding='utf-8')

#Upload the CSV file to Azure cloud
block_blob_service.create_blob_from_path(
    'datasetspowerbi',
    'test.csv',
    '/tmp/test.csv',
     content_settings=ContentSettings(content_type='application/CSV'))
