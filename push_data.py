import os
import json
import sys

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

import certifi
'''

Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts.
Is used by the Python Requests library to verify the identity of the TLS hosts.

'''
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(data.T.to_dict().values()) #json.loads(data.T.to_json()).values()
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.collection = collection
            self.db = database
            self.records = records
                
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)
            self.db = self.mongo_client[self.db]
            self.collection = self.db[self.collection]
            self.collection.insert_many(self.records)

            logging.info("Data inserted successfully")
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    try:
        FILE_PATH = "Network_Data/phisingData.csv"
        DATABASE = "Network_Security"
        COLLECTION = "Network_Data"

        network_data_extract = NetworkDataExtract()
        records = network_data_extract.csv_to_json(FILE_PATH)
        inserted_records = network_data_extract.insert_data_mongodb(records, DATABASE, COLLECTION)

        print(inserted_records)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
