# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.38
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_transaction_receipt import SmartBchTransactionReceipt  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchTransactionReceipt(unittest.TestCase):
    """SmartBchTransactionReceipt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchTransactionReceipt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_transaction_receipt.SmartBchTransactionReceipt()  # noqa: E501
        if include_optional :
            return SmartBchTransactionReceipt(
                to = '0', 
                _from = '0', 
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
                status = 1.337
            )
        else :
            return SmartBchTransactionReceipt(
                to = '0',
                _from = '0',
                contract_address = '0',
                transaction_index = 1.337,
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
        )

    def testSmartBchTransactionReceipt(self):
        """Test SmartBchTransactionReceipt"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
