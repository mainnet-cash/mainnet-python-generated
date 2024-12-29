# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.6.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.token_mint_request import TokenMintRequest  # noqa: E501
from mainnet.rest import ApiException

class TestTokenMintRequest(unittest.TestCase):
    """TokenMintRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TokenMintRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.token_mint_request.TokenMintRequest()  # noqa: E501
        if include_optional :
            return TokenMintRequest(
                wallet_id = '0', 
                token_id = '0', 
                requests = [
                    mainnet.models.token_mint_request_requests.TokenMintRequest_requests(
                        capability = 'none', 
                        commitment = '0', 
                        cashaddr = '0', 
                        value = 1.337, )
                    ], 
                deduct_token_amount = True
            )
        else :
            return TokenMintRequest(
                wallet_id = '0',
                token_id = '0',
        )

    def testTokenMintRequest(self):
        """Test TokenMintRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
