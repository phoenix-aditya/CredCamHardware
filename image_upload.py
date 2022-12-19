from config import database
import base64
import bson
from bson.binary import Binary
from datetime import datetime
import os
import requests

def upload_image_to_ipfs(files):
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
    p = response.json()
    hash = p['Hash']
    return hash

def upload_data_to_mongoDB(
    image_path:str,
    ):
    collection = database.images
    with open(image_path, "rb") as f:
        hash = upload_image_to_ipfs(f.read())
        encoded = base64.b64encode(f.read())
        encoded = encoded.decode('utf-8')
    
    collection.insert_one(
        {
            "username":"aditya" , 
            "file": encoded, 
            "hash": hash,
            "image_capture_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "location": "patiala"
        }
        )

