# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.22
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.wallet_util_api import WalletUtilApi  # noqa: E501
from mainnet.rest import ApiException


class TestWalletUtilApi(unittest.TestCase):
    """WalletUtilApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.wallet_util_api.WalletUtilApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_util_decode_transaction(self):
        """Test case for util_decode_transaction

        Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
