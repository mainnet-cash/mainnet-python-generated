# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.36
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.slp_send_response import SlpSendResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSlpSendResponse(unittest.TestCase):
    """SlpSendResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpSendResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_send_response.SlpSendResponse()  # noqa: E501
        if include_optional :
            return SlpSendResponse(
                tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                balance = mainnet.models.slp_balance_response.SlpBalanceResponse(
                    value = '10000', 
                    ticker = 'MNC', 
                    name = 'Mainnet coin', 
                    token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', 
                    type = 1, ), 
                explorer_url = 'https://testnet.simpleledger.info/#tx/1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f'
            )
        else :
            return SlpSendResponse(
        )

    def testSlpSendResponse(self):
        """Test SlpSendResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
