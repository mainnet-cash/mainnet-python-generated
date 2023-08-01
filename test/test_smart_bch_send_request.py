# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.32
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_send_request import SmartBchSendRequest  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchSendRequest(unittest.TestCase):
    """SmartBchSendRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchSendRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_send_request.SmartBchSendRequest()  # noqa: E501
        if include_optional :
            return SmartBchSendRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45', 
                to = null, 
                options = mainnet.models.smart_bch_send_request_options.SmartBchSendRequestOptions(
                    query_balance = False, 
                    await_transaction_propagation = False, ), 
                overrides = mainnet.models.smart_bch_overrides.SmartBchOverrides(
                    gas_limit = null, 
                    gas_price = null, 
                    max_fee_per_gas = null, 
                    max_priority_fee_per_gas = null, 
                    nonce = null, 
                    value = null, 
                    block_tag = null, 
                    from = '0', )
            )
        else :
            return SmartBchSendRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45',
                to = null,
        )

    def testSmartBchSendRequest(self):
        """Test SmartBchSendRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
