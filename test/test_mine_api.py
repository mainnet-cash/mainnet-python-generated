# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.10
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.mine_api import MineApi  # noqa: E501
from mainnet.rest import ApiException


class TestMineApi(unittest.TestCase):
    """MineApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.mine_api.MineApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mine(self):
        """Test case for mine

        Mine regtest coins to a specified address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
