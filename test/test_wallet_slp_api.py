# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.20
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.wallet_slp_api import WalletSlpApi  # noqa: E501
from mainnet.rest import ApiException


class TestWalletSlpApi(unittest.TestCase):
    """WalletSlpApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.wallet_slp_api.WalletSlpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nft_child_genesis(self):
        """Test case for nft_child_genesis

        Get created tokenId back and new NFT child token balance of the wallet  # noqa: E501
        """
        pass

    def test_nft_parent_genesis(self):
        """Test case for nft_parent_genesis

        Get created tokenId back and new NFT token balance of the wallet  # noqa: E501
        """
        pass

    def test_slp_all_balances(self):
        """Test case for slp_all_balances

        Get all slp balances of the wallet  # noqa: E501
        """
        pass

    def test_slp_balance(self):
        """Test case for slp_balance

        Get total slp token balance of the wallet  # noqa: E501
        """
        pass

    def test_slp_create_wallet(self):
        """Test case for slp_create_wallet

        create a new SLP wallet  # noqa: E501
        """
        pass

    def test_slp_deposit_address(self):
        """Test case for slp_deposit_address

        Get an SLP deposit address in cash address format  # noqa: E501
        """
        pass

    def test_slp_deposit_qr(self):
        """Test case for slp_deposit_qr

        Get an SLP receiving cash address as a qrcode  # noqa: E501
        """
        pass

    def test_slp_genesis(self):
        """Test case for slp_genesis

        Get created tokenId back and new slp token balance of the wallet  # noqa: E501
        """
        pass

    def test_slp_mint(self):
        """Test case for slp_mint

        Get created tokenId back and new slp token balance of the wallet  # noqa: E501
        """
        pass

    def test_slp_outpoints(self):
        """Test case for slp_outpoints

        Get list of unspent SLP outpoints.  # noqa: E501
        """
        pass

    def test_slp_send(self):
        """Test case for slp_send

        Send some SLP token amount to a given cash address  # noqa: E501
        """
        pass

    def test_slp_send_max(self):
        """Test case for slp_send_max

        Send all available SLP funds to a given address  # noqa: E501
        """
        pass

    def test_slp_token_info(self):
        """Test case for slp_token_info

        Get information about the token  # noqa: E501
        """
        pass

    def test_slp_utxos(self):
        """Test case for slp_utxos

        Get detailed information about unspent SLP outputs (utxos)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
