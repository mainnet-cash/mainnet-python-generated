# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.9
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.signed_message_response import SignedMessageResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSignedMessageResponse(unittest.TestCase):
    """SignedMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SignedMessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.signed_message_response.SignedMessageResponse()  # noqa: E501
        if include_optional :
            return SignedMessageResponse(
                signature = 'IA+oq/uGz4kKA2bNgxPcM+T216abyUiBhofMg1J8fC5BLAbbIpF2toCHaO7/LQAxhQBtu5D6ROq1JjXiRwPAASg=', 
                raw = mainnet.models.signed_message_response_raw.SignedMessageResponseRaw(
                    ecdsa = '0', 
                    schnorr = '0', 
                    der = '0', ), 
                details = mainnet.models.signed_message_response_details.SignedMessageResponseDetails(
                    recovery_id = 1.337, 
                    compressed = True, 
                    message_hash = '0', )
            )
        else :
            return SignedMessageResponse(
        )

    def testSignedMessageResponse(self):
        """Test SignedMessageResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
