# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.31
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.wallet_bcmr_api import WalletBcmrApi  # noqa: E501
from mainnet.rest import ApiException


class TestWalletBcmrApi(unittest.TestCase):
    """WalletBcmrApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.wallet_bcmr_api.WalletBcmrApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bcmr_add_metadata_registry_auth_chain(self):
        """Test case for bcmr_add_metadata_registry_auth_chain

        Add BCMR metadata registry from autchain, returning the built chain  # noqa: E501
        """
        pass

    def test_bcmr_add_registry(self):
        """Test case for bcmr_add_registry

        Add BCMR registry from parameter  # noqa: E501
        """
        pass

    def test_bcmr_add_registry_from_uri(self):
        """Test case for bcmr_add_registry_from_uri

        Reset tracked BCMR registries  # noqa: E501
        """
        pass

    def test_bcmr_build_auth_chain(self):
        """Test case for bcmr_build_auth_chain

        Build a BCMR authchain  # noqa: E501
        """
        pass

    def test_bcmr_get_registries(self):
        """Test case for bcmr_get_registries

        Get tracked BCMR registries  # noqa: E501
        """
        pass

    def test_bcmr_get_token_info(self):
        """Test case for bcmr_get_token_info

        Get token info  # noqa: E501
        """
        pass

    def test_bcmr_reset_registries(self):
        """Test case for bcmr_reset_registries

        Reset tracked BCMR registries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
