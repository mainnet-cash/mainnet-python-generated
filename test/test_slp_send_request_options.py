# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.28
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.slp_send_request_options import SlpSendRequestOptions  # noqa: E501
from mainnet.rest import ApiException

class TestSlpSendRequestOptions(unittest.TestCase):
    """SlpSendRequestOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpSendRequestOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_send_request_options.SlpSendRequestOptions()  # noqa: E501
        if include_optional :
            return SlpSendRequestOptions(
                utxo_ids = [
                    'shm:43e724033d3c013cd385bb82d3c1c8a7b3f0e032bc82d9bf4980fca62220648a:0:30000'
                    ]
            )
        else :
            return SlpSendRequestOptions(
        )

    def testSlpSendRequestOptions(self):
        """Test SlpSendRequestOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
