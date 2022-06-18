import pytest
import logging as logger
from api_test2.src.utilities.genericUtility import generate_random_string
from api_test2.src.helpers.product_helper import ProductsHelper
from api_test2.src.dao.products_dao import ProductsDAO

pytestmark = [pytest.mark.product, pytest.mark.smoke]


@pytest.mark.tcid26
def test_create_a_new_product():
    """
    Verify 'POST /products' creates a simple product
    """
    logger.debug("TEST: Create new product")

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make api call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api call response has" \
                                                  f"unexpected name: Expected: {payload['name']}, Actual: {product_rs['name']}"

    # verify the product exists
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)
    assert db_product[0]['post_title'] == payload['name'], f"Create product title DB does not match " \
                                                           f"title in api. DB: {db_product[0]['post_title']}, API: {payload['name']}"
