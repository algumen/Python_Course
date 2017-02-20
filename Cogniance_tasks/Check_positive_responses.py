import requests
import json
from random import randint


def test_positive_responses():
    # The test data:
    candidates_url = "http://qainterview.cogniance.com/candidates"  # Replace this with the real URL
    candidate_name = "Test Name" + str(randint(0, 100000000)) + 'OG'
    candidate_position = "Technical Support"

    # Making the POST request with the test data put to the body:
    resp = requests.post(
        candidates_url,
        json={"name": candidate_name,
              "position": candidate_position}
    )

    # Checking response status code from POST request
    assert 201 == resp.status_code

    # Checking response status code from GET request
    get_candidate = requests.get(candidates_url)
    assert 200 == get_candidate.status_code

    # Checking response status code from GET request with id
    candidates_list = json.loads(get_candidate.content)["candidates"]
    id_0 = str(candidates_list[0]['id'])
    #print(id_0)
    get_candidate = requests.get(candidates_url + '/' + id_0)

    assert 200 == get_candidate.status_code

    # Checking response status code from DELETE request

    del_candidate = requests.delete(candidates_url + '/' + id_0)
    assert 200 == del_candidate.status_code
