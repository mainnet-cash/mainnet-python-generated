# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_sep20_mint_response import SmartBchSep20MintResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchSep20MintResponse(unittest.TestCase):
    """SmartBchSep20MintResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchSep20MintResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_sep20_mint_response.SmartBchSep20MintResponse()  # noqa: E501
        if include_optional :
            return SmartBchSep20MintResponse(
                tx_id = '0xc519c3b66955a598dd1f298fcfaf92530db39b70d6d4699c57ffc5faa5aa30f7', 
                balance = mainnet.models.smart_bch_sep20_balance_response.SmartBchSep20BalanceResponse(
                    value = '10000', 
                    ticker = 'MNC', 
                    name = 'Mainnet coin', 
                    token_id = '0xdac17f958d2ee523a2206206994597c13d831ec7', )
            )
        else :
            return SmartBchSep20MintResponse(
        )

    def testSmartBchSep20MintResponse(self):
        """Test SmartBchSep20MintResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
