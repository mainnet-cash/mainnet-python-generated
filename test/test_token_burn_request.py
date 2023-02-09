# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.11
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.token_burn_request import TokenBurnRequest  # noqa: E501
from mainnet.rest import ApiException

class TestTokenBurnRequest(unittest.TestCase):
    """TokenBurnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TokenBurnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.token_burn_request.TokenBurnRequest()  # noqa: E501
        if include_optional :
            return TokenBurnRequest(
                wallet_id = '0', 
                token_id = '0', 
                capability = 'none', 
                commitment = '0', 
                amount = 1.337, 
                cashaddr = '0', 
                message = '0'
            )
        else :
            return TokenBurnRequest(
                wallet_id = '0',
                token_id = '0',
        )

    def testTokenBurnRequest(self):
        """Test TokenBurnRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
