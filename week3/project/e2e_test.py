"""
Script to send a batch of requests to web app, hosted in docker container
"""

import requests
import json

examples = []
with open("data/requests.json", "r") as f:
    for line in f:
        examples.append(json.loads(line))

for example in examples:
    r = requests.post("http://0.0.0.0/predict", data=json.dumps(example))
