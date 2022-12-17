from config import database
import base64
import bson
from bson.binary import Binary
from datetime import datetime
import os

def upload_image_to_ipfs():
    return ""

def upload_data_to_mongoDB(
    image_path:str,
    ):
    collection = database.images
    with open(image_path, "rb") as f:
        encoded = Binary(f.read())

    collection.insert_one(
        {
            "username":"aditya" , 
            "file": encoded, 
            "image_capture_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "location": "patiala"
        }
        )

