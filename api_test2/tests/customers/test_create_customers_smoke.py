import pytest
import logging as logger
from api_test2.src.utilities import genericUtility
from api_test2.src.helpers import customer_helper
from api_test2.src.dao.customers_dao import CustomerDAO
from api_test2.src.utilities import request_utility

"""Create customer """


@pytest.mark.tcid_29
@pytest.mark.customer
def test_create_customer_only_email_password():
    """
    Verify 'POST /customers' creates user with email and password only
    """
    logger.debug("TEST: Create new customer with email and password only")
    random_info = genericUtility.generate_random_email_and_password()
    print(random_info)
    email = random_info['email']
    password = random_info['password']

    # make the call to create customer payload
    cust_obj = customer_helper.CustomerHelper()
    cust_obj_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email in the response
    assert cust_obj_api_info['email'] == email, f"Create customer api response returns wrong email: {email}"

    # verify email and first name in the response
    assert cust_obj_api_info['first_name'] == '', f"Create customer api response returns value for first name" \
                                                  f"but it should be empty."

    # verify customer is created in database
    cust_dao = CustomerDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    # import pdb;
    # pdb.set_trace()
    id_in_api = cust_obj_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.' \
                                  f'Email: {email}'
    # import pdb; pdb.set_trace()


@pytest.mark.tcid47
@pytest.mark.customer
def test_create_customer_fail_for_existing_email():
    """
    Veirfy 'create customer' fails if email exists
    """
    # get an existing email from DB
    cust_dao = CustomerDAO()
    existing_customer = cust_dao.get_random_customer_from_db()
    existing_email = existing_customer[0]['user_email']

    # call the api
    req_helper = request_utility.RequestUtility()

    payload = {"email": existing_email, "password": "Password1"}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    """
    cust_api_info returns below
    {'code': 'registration-error-email-exists', 'message': 'An account is already registered with your email address. 
    <a href="#" class="showlogin">Please log in.</a>', 'data': {'status': 400}}
    """

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with " \
                                                                       f"existing user error 'code' is not correct. Expected: 'registration-error-email-exists' but " \
                                                                       f"Actual: {cust_api_info['code']}"
    assert 'An account is already registered with your email address' in cust_api_info[
        'message'], f"Create customer with " \
                    f"existing user error 'message' is not correct. Expected: 'An account is already registered with \
        your email address' but" \
                    f"Actual: {cust_api_info['message']}"

