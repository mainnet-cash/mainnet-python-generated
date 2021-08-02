# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.40
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.faucet_api import FaucetApi  # noqa: E501
from mainnet.rest import ApiException


class TestFaucetApi(unittest.TestCase):
    """FaucetApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.faucet_api.FaucetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_addresses(self):
        """Test case for get_addresses

        Get addresses to return back or donate the testnet bch and tokens   # noqa: E501
        """
        pass

    def test_get_testnet_bch(self):
        """Test case for get_testnet_bch

        Get testnet bch   # noqa: E501
        """
        pass

    def test_get_testnet_slp(self):
        """Test case for get_testnet_slp

        Get testnet slp tokens   # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
