import requests
import json
from random import randint


def test_negative_response_1():

    # Making the POST request with application/json is absent
    resp = requests.post(
        candidates_url
    )

    # Checking response status code
    assert 400 == resp.status_code
