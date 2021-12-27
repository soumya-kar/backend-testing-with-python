import logging as logger
import pytest
from api_test2.src.utilities.request_utility import RequestUtility

"""List all customers"""
@pytest.mark.tcid30
@pytest.mark.customer
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('customers')

    # assert rs_api is not empty
    assert rs_api, f"Response of list all customer is empty"
    # import pdb;
    # pdb.set_trace()