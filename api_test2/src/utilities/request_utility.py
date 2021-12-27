import json
import os
import requests
from api_test2.src.configs.hosts_config import API_HOSTS
from api_test2.src.utilities.credentialsUtility import CredentialsUtility
from requests_oauthlib import OAuth1
import logging as logger


class RequestUtility(object):

    def __init__(self):
        api_keys = CredentialsUtility.get_wc_api_keys(self)
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS.get(self.env)
        self.auth = OAuth1(api_keys['wc_key'], api_keys['wc_secret'])

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        # import pdb; pdb.set_trace()
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint
        rs_api = requests.post(url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code} but Actual {self.status_code}'
        # import pdb;
        # pdb.set_trace()
        logger.debug(f"****************POST API RESPONSE**************: {rs_api.json()}")
        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint
        rs_api = requests.get(url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(
            expected_status_code), f'Expected status code {expected_status_code} but Actual {self.status_code}'
        # import pdb;
        # pdb.set_trace()
        logger.debug(f"***********GET API RESPONSE*****************: {rs_api.json()}")
        return rs_api.json()