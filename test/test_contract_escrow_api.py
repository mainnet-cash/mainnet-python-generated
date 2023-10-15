# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.2.5
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.contract_escrow_api import ContractEscrowApi  # noqa: E501
from mainnet.rest import ApiException


class TestContractEscrowApi(unittest.TestCase):
    """ContractEscrowApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.contract_escrow_api.ContractEscrowApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_escrow(self):
        """Test case for create_escrow

        Create an escrow contract  # noqa: E501
        """
        pass

    def test_escrow_fn(self):
        """Test case for escrow_fn

        Finalize an escrow contract  # noqa: E501
        """
        pass

    def test_escrow_info(self):
        """Test case for escrow_info

        Get information about an escrow contract from the escrowContractId  # noqa: E501
        """
        pass

    def test_escrow_utxos(self):
        """Test case for escrow_utxos

        List specific utxos on any escrow contract  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
