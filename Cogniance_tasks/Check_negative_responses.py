import requests
import json
from random import randint


def test_negative_responses():
    # The test data:
    candidates_url = "http://qainterview.cogniance.com/candidates"  # Replace this with the real URL
    candidate_name = ""
    candidate_position = "Technical Support"

    # Making the POST request with the test data put to the body:
    resp = requests.post(
        candidates_url,
        json={"name": candidate_name,
              "position": candidate_position}
    )

    # Checking response status code
    assert 400 == resp.status_code
