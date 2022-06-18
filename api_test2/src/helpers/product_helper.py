from api_test2.src.utilities.request_utility import RequestUtility
import logging as logger


class ProductsHelper(object):

    def __init__(self):
        self.request_util = RequestUtility()

    def get_product_by_id(self, product_id):
        return self.request_util.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.request_util.post(endpoint='products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):
        # return self.request_util.get('products', payload=payload)
        max_pages = 1000
        all_products = []

        for i in range(1, max_pages + 1):
            logger.debug(f"List product page number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 3

            # add current page number to the call

            payload['page'] = i
            rs_api = self.request_util.get('products', payload=payload)

            # if there is not response then stop loop b/c there are no more products

            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products
