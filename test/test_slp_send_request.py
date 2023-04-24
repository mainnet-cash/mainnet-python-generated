# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.7
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.slp_send_request import SlpSendRequest  # noqa: E501
from mainnet.rest import ApiException

class TestSlpSendRequest(unittest.TestCase):
    """SlpSendRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpSendRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_send_request.SlpSendRequest()  # noqa: E501
        if include_optional :
            return SlpSendRequest(
                wallet_id = 'wif:testnet:cNfsPtqN2bMRS7vH5qd8tR8GMvgXyL5BjnGAKgZ8DYEiCrCCQcP6', 
                to = [
                    mainnet.models.slp_send_request_item.SlpSendRequestItem(
                        slpaddr = 'slptest:qqm4gsaa2gvk7flvsvj7f0w4rlq32vqhkq32uar866', 
                        value = 100, 
                        token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', )
                    ]
            )
        else :
            return SlpSendRequest(
                wallet_id = 'wif:testnet:cNfsPtqN2bMRS7vH5qd8tR8GMvgXyL5BjnGAKgZ8DYEiCrCCQcP6',
                to = [
                    mainnet.models.slp_send_request_item.SlpSendRequestItem(
                        slpaddr = 'slptest:qqm4gsaa2gvk7flvsvj7f0w4rlq32vqhkq32uar866', 
                        value = 100, 
                        token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15', )
                    ],
        )

    def testSlpSendRequest(self):
        """Test SlpSendRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
