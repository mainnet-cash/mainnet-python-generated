# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.11
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.slp_mint_response import SlpMintResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSlpMintResponse(unittest.TestCase):
    """SlpMintResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpMintResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_mint_response.SlpMintResponse()  # noqa: E501
        if include_optional :
            return SlpMintResponse(
                tx_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', 
                balance = mainnet.models.slp_balance_response.SlpBalanceResponse(
                    value = '10000', 
                    ticker = 'MNC', 
                    name = 'Mainnet coin', 
                    token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', 
                    type = 1, )
            )
        else :
            return SlpMintResponse(
        )

    def testSlpMintResponse(self):
        """Test SlpMintResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
