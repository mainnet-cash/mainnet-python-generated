# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.wallet_signed_api import WalletSignedApi  # noqa: E501
from mainnet.rest import ApiException


class TestWalletSignedApi(unittest.TestCase):
    """WalletSignedApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.wallet_signed_api.WalletSignedApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_signed_message_sign(self):
        """Test case for signed_message_sign

        Returns the message signature  # noqa: E501
        """
        pass

    def test_signed_message_verify(self):
        """Test case for signed_message_verify

        Returns a boolean indicating whether message was valid for a given address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
