# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.31
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.get_testnet_sbch_response import GetTestnetSbchResponse  # noqa: E501
from mainnet.rest import ApiException

class TestGetTestnetSbchResponse(unittest.TestCase):
    """GetTestnetSbchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetTestnetSbchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.get_testnet_sbch_response.GetTestnetSbchResponse()  # noqa: E501
        if include_optional :
            return GetTestnetSbchResponse(
                success = True
            )
        else :
            return GetTestnetSbchResponse(
        )

    def testGetTestnetSbchResponse(self):
        """Test GetTestnetSbchResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
