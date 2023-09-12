# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.send_response import SendResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSendResponse(unittest.TestCase):
    """SendResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SendResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.send_response.SendResponse()  # noqa: E501
        if include_optional :
            return SendResponse(
                tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                balance = mainnet.models.balance_response.BalanceResponse(
                    bch = 1, 
                    sat = 100000000, 
                    usd = 438.02, ), 
                explorer_url = 'https://www.blockchain.com/bch-testnet/tx/1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                token_ids = [
                    '["132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15"]'
                    ]
            )
        else :
            return SendResponse(
        )

    def testSendResponse(self):
        """Test SendResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
