import pytest
from api_test2.src.utilities.request_utility import RequestUtility
from api_test2.src.dao.products_dao import ProductsDAO
from api_test2.src.helpers.product_helper import ProductsHelper

pytestmark = [pytest.mark.product, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    """
    Verify 'GET /products' does not return empty
    """
    req_helper = RequestUtility()
    rs_api = req_helper.get('products')

    # assert rs_api is not empty
    assert rs_api, f"Response of list all products api is empty"


@pytest.mark.tcid25
def test_get_product_by_id():
    """
    Verify 'products/id' returns a product with the given id
    """
    # get a product (test data) from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_prod_id_db = rand_product[0]['ID']
    rand_prod_name_db = rand_product[0]['post_title']

    # make the call
    rs_api = ProductsHelper().get_product_by_id(rand_prod_id_db)
    rand_prod_name_api = rs_api['name']

    # verify the response
    assert rand_prod_name_db == rand_prod_name_api, f"Response name is not correct, Expected was {rand_prod_name_db}" \
                                                  f"But Actual is: {rand_prod_name_api}"
