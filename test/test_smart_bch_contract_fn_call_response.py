# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_contract_fn_call_response import SmartBchContractFnCallResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchContractFnCallResponse(unittest.TestCase):
    """SmartBchContractFnCallResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchContractFnCallResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_contract_fn_call_response.SmartBchContractFnCallResponse()  # noqa: E501
        if include_optional :
            return SmartBchContractFnCallResponse(
                contract_id = '0', 
                result = null, 
                tx_id = '0xc519c3b66955a598dd1f298fcfaf92530db39b70d6d4699c57ffc5faa5aa30f7', 
                receipt = mainnet.models.smart_bch_transaction_receipt.SmartBchTransactionReceipt(
                    to = '0', 
                    from = '0', 
                    contract_address = '0', 
                    transaction_index = 1.337, 
                    root = '0', 
                    gas_used = '0', 
                    logs_bloom = '0', 
                    block_hash = '0', 
                    transaction_hash = '0', 
                    logs = [
                        null
                        ], 
                    block_number = 1.337, 
                    confirmations = 1.337, 
                    cumulative_gas_used = '0', 
                    effective_gas_price = '0', 
                    byzantium = True, 
                    type = 1.337, 
                    status = 1.337, )
            )
        else :
            return SmartBchContractFnCallResponse(
        )

    def testSmartBchContractFnCallResponse(self):
        """Test SmartBchContractFnCallResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
