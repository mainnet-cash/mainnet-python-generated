# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.15
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.watch_address_request import WatchAddressRequest  # noqa: E501
from mainnet.rest import ApiException

class TestWatchAddressRequest(unittest.TestCase):
    """WatchAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WatchAddressRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.watch_address_request.WatchAddressRequest()  # noqa: E501
        if include_optional :
            return WatchAddressRequest(
                cashaddr = 'bchtest:qzd0tv75gx6y0zspzwqpgkwkq0n72g8fsq2zch26s2', 
                url = 'http://example.com/webhook', 
                type = 'transaction:in,out', 
                recurrence = 'once', 
                token_id = null, 
                duration_sec = 86400
            )
        else :
            return WatchAddressRequest(
                cashaddr = 'bchtest:qzd0tv75gx6y0zspzwqpgkwkq0n72g8fsq2zch26s2',
                url = 'http://example.com/webhook',
                type = 'transaction:in,out',
        )

    def testWatchAddressRequest(self):
        """Test WatchAddressRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
