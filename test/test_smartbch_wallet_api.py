# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.26
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.smartbch_wallet_api import SmartbchWalletApi  # noqa: E501
from mainnet.rest import ApiException


class TestSmartbchWalletApi(unittest.TestCase):
    """SmartbchWalletApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.smartbch_wallet_api.SmartbchWalletApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_smartbch_balance(self):
        """Test case for smartbch_balance

        Get total balance for wallet  # noqa: E501
        """
        pass

    def test_smartbch_create_wallet(self):
        """Test case for smartbch_create_wallet

        create a new wallet  # noqa: E501
        """
        pass

    def test_smartbch_deposit_address(self):
        """Test case for smartbch_deposit_address

        Get a deposit address  # noqa: E501
        """
        pass

    def test_smartbch_deposit_qr(self):
        """Test case for smartbch_deposit_qr

        Get receiving cash address as a qrcode  # noqa: E501
        """
        pass

    def test_smartbch_max_amount_to_send(self):
        """Test case for smartbch_max_amount_to_send

        Get maximum spendable amount  # noqa: E501
        """
        pass

    def test_smartbch_send(self):
        """Test case for smartbch_send

        Send some amount to a given address  # noqa: E501
        """
        pass

    def test_smartbch_send_max(self):
        """Test case for smartbch_send_max

        Send all available funds to a given address  # noqa: E501
        """
        pass

    def test_smartbch_signed_message_sign(self):
        """Test case for smartbch_signed_message_sign

        Returns the message signature  # noqa: E501
        """
        pass

    def test_smartbch_signed_message_verify(self):
        """Test case for smartbch_signed_message_verify

        Returns a boolean indicating whether message was valid for a given address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
