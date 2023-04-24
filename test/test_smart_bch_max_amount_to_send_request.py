# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.5
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_max_amount_to_send_request import SmartBchMaxAmountToSendRequest  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchMaxAmountToSendRequest(unittest.TestCase):
    """SmartBchMaxAmountToSendRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchMaxAmountToSendRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_max_amount_to_send_request.SmartBchMaxAmountToSendRequest()  # noqa: E501
        if include_optional :
            return SmartBchMaxAmountToSendRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45'
            )
        else :
            return SmartBchMaxAmountToSendRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45',
        )

    def testSmartBchMaxAmountToSendRequest(self):
        """Test SmartBchMaxAmountToSendRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
