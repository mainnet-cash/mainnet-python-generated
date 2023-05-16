# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.21
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.contract_fn_response import ContractFnResponse  # noqa: E501
from mainnet.rest import ApiException

class TestContractFnResponse(unittest.TestCase):
    """ContractFnResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractFnResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.contract_fn_response.ContractFnResponse()  # noqa: E501
        if include_optional :
            return ContractFnResponse(
                contract_id = '0', 
                tx_id = '1e6442a0d3548bb4f917721184ac1cb163ddf324e2c09f55c46ff0ba521cb89f', 
                hex = '0200000001f6d804c0a2f33936dd8b535d1... bdf0e43b30135be5251', 
                debug = 'meep debug --tx=0200000001b3f2d1ce4951d104e8244310943c49cd8ea59b437fa5b794197fcffc32cfc28900000000b941b0e8a077ea6d70c757487a14c175c9ed21a5f4f54d0477578ac3bc89da86cbb5567f62eb9b46c49c328f02165a54a577cc4228fd2dd5a5497fc25a638f0205b1412103410ef048b3da351793f6ed14cc2fde460becc5b658d9138443b9a3000707a6a7514c5202d70014a72d8e8dc9ca261e8ffafba96514ee92b0c2bf271456b6b22042b90dd67bf2fbfb9aff7d37fbee11245379009c63557a5579ad547aa97b8777777767537a519d547a5479ad537aa9887cb16d5168feffffff0268420000000000001976a91456b6b22042b90dd67bf2fbfb9aff7d37fbee112488ac720e00000000000017a914d411d850ed6395e6e72a5e0497a54ab99a75b84387d7000000 --idx=0 --amt=21000 --pkscript=a914d411d850ed6395e6e72a5e0497a54ab99a75b84387
'
            )
        else :
            return ContractFnResponse(
        )

    def testContractFnResponse(self):
        """Test ContractFnResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
