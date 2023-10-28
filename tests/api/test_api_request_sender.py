import json
import logging

import pytest

from requests.exceptions import RequestException

from metapython.api.api_request_sender import ApiRequestSender
from metapython.api.consts import API_URL, APIEndpoint


class Stub(object): 

    def raise_for_status(self):
        pass


def stub(*args): pass


PAGE_ACCESS_TOKEN = "123456"

def test_post_request_success(monkeypatch):
    def callback(endpoint,params,json):
        assert endpoint == API_URL + APIEndpoint.MESSAGES

        response = Stub()
        response.raise_for_status = stub
        response.text = '{"message": "success"}'

        return response

    monkeypatch.setattr("requests.post", callback)

    request_sender = ApiRequestSender(PAGE_ACCESS_TOKEN)


    response = request_sender.post_request(API_URL + APIEndpoint.MESSAGES, {})


    assert response == {"message": "success"}

