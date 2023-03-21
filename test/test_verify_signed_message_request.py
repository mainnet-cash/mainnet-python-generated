# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.18
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.verify_signed_message_request import VerifySignedMessageRequest  # noqa: E501
from mainnet.rest import ApiException

class TestVerifySignedMessageRequest(unittest.TestCase):
    """VerifySignedMessageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VerifySignedMessageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.verify_signed_message_request.VerifySignedMessageRequest()  # noqa: E501
        if include_optional :
            return VerifySignedMessageRequest(
                wallet_id = 'watch:mainnet:bitcoincash:qqehccy89v7ftlfgr9v0zvhjzyy7eatdkqt05lt3nw', 
                message = 'Chancellor on brink of second bailout for banks', 
                signature = IA+oq/uGz4kKA2bNgxPcM+T216abyUiBhofMg1J8fC5BLAbbIpF2toCHaO7/LQAxhQBtu5D6ROq1JjXiRwPAASg=, 
                public_key = '0'
            )
        else :
            return VerifySignedMessageRequest(
        )

    def testVerifySignedMessageRequest(self):
        """Test VerifySignedMessageRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
