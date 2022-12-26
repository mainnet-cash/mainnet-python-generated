# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mainnet
from mainnet.api.smartbch_contract_api import SmartbchContractApi  # noqa: E501
from mainnet.rest import ApiException


class TestSmartbchContractApi(unittest.TestCase):
    """SmartbchContractApi unit test stubs"""

    def setUp(self):
        self.api = mainnet.api.smartbch_contract_api.SmartbchContractApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_smart_bch_contract_call(self):
        """Test case for smart_bch_contract_call

        Call a SmartBch contract function  # noqa: E501
        """
        pass

    def test_smart_bch_contract_create(self):
        """Test case for smart_bch_contract_create

        Create a SmartBch contractId  # noqa: E501
        """
        pass

    def test_smart_bch_contract_deploy(self):
        """Test case for smart_bch_contract_deploy

        Request to deploy a SmartBch contract  # noqa: E501
        """
        pass

    def test_smart_bch_contract_estimate_gas(self):
        """Test case for smart_bch_contract_estimate_gas

        Estimate the gas for a contract interaction function given the arguments  # noqa: E501
        """
        pass

    def test_smart_bch_contract_info(self):
        """Test case for smart_bch_contract_info

        Get information about a SmartBch contract from the contractId  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
