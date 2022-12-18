# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
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

    def test_encode_transaction(self):
        """Test case for encode_transaction

        Encode and sign a transaction given a list of sendRequests, options and estimate fees  # noqa: E501
        """
        pass

    def test_get_all_nft_token_balances(self):
        """Test case for get_all_nft_token_balances

        Get non-fungible token balance  # noqa: E501
        """
        pass

    def test_get_all_token_balances(self):
        """Test case for get_all_token_balances

        Get non-fungible token balance  # noqa: E501
        """
        pass

    def test_get_history(self):
        """Test case for get_history

        Get a simplified list of transactions related to a wallet  # noqa: E501
        """
        pass

    def test_get_nft_token_balance(self):
        """Test case for get_nft_token_balance

        Get non-fungible token balance  # noqa: E501
        """
        pass

    def test_get_token_balance(self):
        """Test case for get_token_balance

        Get fungible token balance  # noqa: E501
        """
        pass

    def test_get_token_utxos(self):
        """Test case for get_token_utxos

        Get token utxos  # noqa: E501
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

    def test_submit_transaction(self):
        """Test case for submit_transaction

        submit an encoded and signed transaction to the network  # noqa: E501
        """
        pass

    def test_token_burn(self):
        """Test case for token_burn

        Perform an explicit token burn  # noqa: E501
        """
        pass

    def test_token_deposit_address(self):
        """Test case for token_deposit_address

        Get a token aware deposit address in cash address format  # noqa: E501
        """
        pass

    def test_token_deposit_qr(self):
        """Test case for token_deposit_qr

        Get receiving token aware cash address as a qrcode  # noqa: E501
        """
        pass

    def test_token_genesis(self):
        """Test case for token_genesis

        Create new token category  # noqa: E501
        """
        pass

    def test_token_mint(self):
        """Test case for token_mint

        Mint new non-fungible tokens  # noqa: E501
        """
        pass

    def test_utxos(self):
        """Test case for utxos

        Get detailed information about unspent outputs (utxos)  # noqa: E501
        """
        pass

    def test_xpubkeys(self):
        """Test case for xpubkeys

        A set of xpubkeys and paths for the wallet.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
