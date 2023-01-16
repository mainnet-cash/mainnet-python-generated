# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.encode_transaction_request import EncodeTransactionRequest  # noqa: E501
from mainnet.rest import ApiException

class TestEncodeTransactionRequest(unittest.TestCase):
    """EncodeTransactionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EncodeTransactionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.encode_transaction_request.EncodeTransactionRequest()  # noqa: E501
        if include_optional :
            return EncodeTransactionRequest(
                wallet_id = 'wif:testnet:cNfsPtqN2bMRS7vH5qd8tR8GMvgXyL5BjnGAKgZ8DYEiCrCCQcP6', 
                discard_change = True, 
                to = null, 
                options = mainnet.models.send_request_options.SendRequestOptions(
                    utxo_ids = [
                        '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f:0:5000'
                        ], 
                    change_address = 'bchtest:qzd0tv75gx6y0zspzwqpgkwkq0n72g8fsq2zch26s2', 
                    slp_aware = True, 
                    slp_semi_aware = True, 
                    query_balance = False, 
                    await_transaction_propagation = False, 
                    fee_paid_by = 'change', 
                    check_token_quantities = True, )
            )
        else :
            return EncodeTransactionRequest(
        )

    def testEncodeTransactionRequest(self):
        """Test EncodeTransactionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
