from typing import Any
from random import choice, random
from fastapi import UploadFile
import requests as req

def classify(image: UploadFile) -> dict:
    res = req.post(
        'http://localhost:8000/classify',
        files={'image': image.file},
    )
    if res.status_code != 200:
        raise Exception(f'Failed to classify. Error: {res.text}')
    
    return res.json()
