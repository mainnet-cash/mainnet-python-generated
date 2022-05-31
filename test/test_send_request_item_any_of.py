# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.5.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.send_request_item_any_of import SendRequestItemAnyOf  # noqa: E501
from mainnet.rest import ApiException

class TestSendRequestItemAnyOf(unittest.TestCase):
    """SendRequestItemAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SendRequestItemAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.send_request_item_any_of.SendRequestItemAnyOf()  # noqa: E501
        if include_optional :
            return SendRequestItemAnyOf(
                cashaddr = 'bchtest:qpalhxhl05mlhms3ys43u76rn0ttdv3qg2usm4nm7t', 
                value = 100
            )
        else :
            return SendRequestItemAnyOf(
                cashaddr = 'bchtest:qpalhxhl05mlhms3ys43u76rn0ttdv3qg2usm4nm7t',
                value = 100,
        )

    def testSendRequestItemAnyOf(self):
        """Test SendRequestItemAnyOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
