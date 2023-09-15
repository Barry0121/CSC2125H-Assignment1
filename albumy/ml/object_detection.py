import requests
import json
import os

def load_api_key():
    # Laod api keys form azure vision endpoint
    if 'api-key.key' not in os.listdir():
        raise FileNotFoundError("Cannot find file 'api-key.key', please create this file at root directory.")

    with open('api-key.key', 'rb') as json_file:
        d = json.load(json_file)
    return d['key']

def query(filename):
    with open(filename, "rb") as f:
        image = f.read()
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    headers = {"Authorization": f"{load_api_key()}"}
    response = requests.post(API_URL, headers=headers, data=image)
    res = response.json()
    return list(set([d['label'] for d in res]))

