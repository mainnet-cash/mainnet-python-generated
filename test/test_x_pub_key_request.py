# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.4.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.x_pub_key_request import XPubKeyRequest  # noqa: E501
from mainnet.rest import ApiException

class TestXPubKeyRequest(unittest.TestCase):
    """XPubKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XPubKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.x_pub_key_request.XPubKeyRequest()  # noqa: E501
        if include_optional :
            return XPubKeyRequest(
                wallet_id = 'seed:testnet:anchor stone process they donkey foam danger boat palace kind west cute:m/44'/0'/0'/0/0', 
                paths = [
                    'm/44'/0'/0''
                    ]
            )
        else :
            return XPubKeyRequest(
                wallet_id = 'seed:testnet:anchor stone process they donkey foam danger boat palace kind west cute:m/44'/0'/0'/0/0',
        )

    def testXPubKeyRequest(self):
        """Test XPubKeyRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
