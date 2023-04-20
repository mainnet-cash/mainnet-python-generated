# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_sep20_genesis_response import SmartBchSep20GenesisResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchSep20GenesisResponse(unittest.TestCase):
    """SmartBchSep20GenesisResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchSep20GenesisResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_sep20_genesis_response.SmartBchSep20GenesisResponse()  # noqa: E501
        if include_optional :
            return SmartBchSep20GenesisResponse(
                token_id = '0xdac17f958d2ee523a2206206994597c13d831ec7', 
                balance = mainnet.models.smart_bch_sep20_balance_response.SmartBchSep20BalanceResponse(
                    value = '10000', 
                    ticker = 'MNC', 
                    name = 'Mainnet coin', 
                    token_id = '0xdac17f958d2ee523a2206206994597c13d831ec7', )
            )
        else :
            return SmartBchSep20GenesisResponse(
        )

    def testSmartBchSep20GenesisResponse(self):
        """Test SmartBchSep20GenesisResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
