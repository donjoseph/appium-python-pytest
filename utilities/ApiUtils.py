import json

import requests


def standardHeaders():
    return {'accept': 'application/json'}


def httpPost(URL, headers=standardHeaders(), payload={}, PARAMS={}):
    response = requests.post(url=URL,
                             headers=headers,
                             data=json.dumps(payload, indent=4),
                             params=PARAMS)
    return response


def httpGet(URL, headers=standardHeaders(), PARAMS={}):
    response = requests.get(url=URL,
                            headers=headers,
                            params=PARAMS)
    return response


def httpPut(URL, headers=standardHeaders(), payload={}, PARAMS={}):
    response = requests.put(url=URL,
                            headers=headers,
                            data=json.dumps(payload, indent=4),
                            params=PARAMS)
    return response


def httpStatusValidation(response):
    assert response.status_code in [200, 201], "Response code validation failed"
