import requests
import json
from random import randint


def test_brute_force():
    i = 0
    while i < 100:
        candidates_url = "http://qainterview.cogniance.com/candidates"  # Replace this with the real URL
        candidate_name = "Test Name" + str(randint(0, 100000000)) + 'OG'
        candidate_position = "Technical Support" + str(randint(0, 100000000)) + 'OG'
        resp = requests.post(candidates_url, json={"name": candidate_name, "position": candidate_position})
        assert 201 == resp.status_code

        get_candidate = requests.get(candidates_url)

        candidates_list = json.loads(get_candidate.content)["candidates"]

        candidates_qty = int(len(json.dumps(candidates_list))) #Тут якась фігня із визначенням кількості записів - не встиг розібратись

        new_candidate_id = int(candidates_list[candidates_qty - 1]['id'])

        assert candidate_name == str(candidates_list[new_candidate_id]["name"]) and candidate_position == str(
            candidates_list[new_candidate_id]["position"])

        del_candidate = requests.delete(candidates_url + '/' + str(new_candidate_id))
        assert 200 == del_candidate.status_code

        i += 1


