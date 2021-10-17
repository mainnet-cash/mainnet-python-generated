# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.23
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.contract_fn_request import ContractFnRequest  # noqa: E501
from mainnet.rest import ApiException

class TestContractFnRequest(unittest.TestCase):
    """ContractFnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractFnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.contract_fn_request.ContractFnRequest()  # noqa: E501
        if include_optional :
            return ContractFnRequest(
                contract_id = '0', 
                action = 'send', 
                function = '0', 
                arguments = [
                    '0'
                    ], 
                to = null, 
                utxo_ids = [
                    '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f:0:1000'
                    ], 
                op_return = [
                    '0'
                    ], 
                fee_per_byte = 1.337, 
                hardcoded_fee = 1.337, 
                min_change = 1.337, 
                without_change = True, 
                age = 1.337, 
                time = 1.337
            )
        else :
            return ContractFnRequest(
                contract_id = '0',
                function = '0',
                to = null,
        )

    def testContractFnRequest(self):
        """Test ContractFnRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
