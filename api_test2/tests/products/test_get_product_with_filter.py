import pytest
from datetime import datetime, timedelta
from api_test2.src.helpers.product_helper import ProductsHelper
from api_test2.src.dao.products_dao import ProductsDAO


@pytest.mark.regression
class TestListProductWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_after_filter(self):
        """
        Verify  'List Products' with filter 'after'
        """
        # create data
        x_days_from_today = 1500
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = tmp_date.strftime('%Y-%M-%dT%H:%m:%S')

        # make the call
        payload = dict()
        payload['after'] = after_created_date
        # payload['per_page'] = 100
        rs_api = ProductsHelper().call_list_products(payload)
        assert rs_api, f"Empty response for 'list products with filter'"

        # get data from DB
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # verify response
        assert len(rs_api) == len(db_products), f"List product with after filter does not match with db, " \
                                                f"Expected DB response {len(db_products)}"\
                                                f"Actual API response: {len(rs_api)}"

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]
        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter, product ids in response mismatch in db"