# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.13
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.verify_signed_message_response import VerifySignedMessageResponse  # noqa: E501
from mainnet.rest import ApiException

class TestVerifySignedMessageResponse(unittest.TestCase):
    """VerifySignedMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VerifySignedMessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.verify_signed_message_response.VerifySignedMessageResponse()  # noqa: E501
        if include_optional :
            return VerifySignedMessageResponse(
                valid = True, 
                details = mainnet.models.verify_signed_message_response_details.VerifySignedMessageResponseDetails(
                    signature_type = '0', 
                    message_hash = '0', 
                    signature_valid = True, 
                    public_key_hash_match = True, )
            )
        else :
            return VerifySignedMessageResponse(
        )

    def testVerifySignedMessageResponse(self):
        """Test VerifySignedMessageResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
