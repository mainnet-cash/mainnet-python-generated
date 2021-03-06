# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.28
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.wallet_api import WalletApi  # noqa: E501
from mainnet.rest import ApiException


class TestWalletApi(unittest.TestCase):
    """WalletApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.wallet_api.WalletApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_balance(self):
        """Test case for balance

        Get total balance for wallet  # noqa: E501
        """
        pass

    def test_create_wallet(self):
        """Test case for create_wallet

        create a new wallet  # noqa: E501
        """
        pass

    def test_deposit_address(self):
        """Test case for deposit_address

        Get a deposit address in cash address format  # noqa: E501
        """
        pass

    def test_deposit_qr(self):
        """Test case for deposit_qr

        Get receiving cash address as a qrcode  # noqa: E501
        """
        pass

    def test_info(self):
        """Test case for info

        Get information about a wallet  # noqa: E501
        """
        pass

    def test_max_amount_to_send(self):
        """Test case for max_amount_to_send

        Get maximum spendable amount  # noqa: E501
        """
        pass

    def test_named_exists(self):
        """Test case for named_exists

        Check if a named wallet already exists  # noqa: E501
        """
        pass

    def test_replace_named(self):
        """Test case for replace_named

        Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a `walletId` supplied If wallet exists it will be overwritten without exception   # noqa: E501
        """
        pass

    def test_send(self):
        """Test case for send

        Send some amount to a given address  # noqa: E501
        """
        pass

    def test_send_max(self):
        """Test case for send_max

        Send all available funds to a given address  # noqa: E501
        """
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

    def test_utxos(self):
        """Test case for utxos

        Get detailed information about unspent outputs (utxos)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
