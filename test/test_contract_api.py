# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.contract_api import ContractApi  # noqa: E501
from mainnet.rest import ApiException


class TestContractApi(unittest.TestCase):
    """ContractApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.contract_api.ContractApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contract_fn(self):
        """Test case for contract_fn

        Call a method on a contract  # noqa: E501
        """
        pass

    def test_contract_info(self):
        """Test case for contract_info

        Get information about a contract from the contractId  # noqa: E501
        """
        pass

    def test_contract_utxos(self):
        """Test case for contract_utxos

        List specific utxos on any contract  # noqa: E501
        """
        pass

    def test_create_contract(self):
        """Test case for create_contract

        Create a cashscript contract  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
