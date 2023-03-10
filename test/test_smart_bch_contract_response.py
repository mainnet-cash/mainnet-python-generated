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
from mainnet.models.smart_bch_contract_response import SmartBchContractResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchContractResponse(unittest.TestCase):
    """SmartBchContractResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchContractResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_contract_response.SmartBchContractResponse()  # noqa: E501
        if include_optional :
            return SmartBchContractResponse(
                contract_id = 'smartbchcontract:mainnet:0xdac17f958d2ee523a2206206994597c13d831ec7:WyJmdW5jdGlvbiBuYW1lKCkgdmlldyByZXR1cm5zIChzdHJpbmcpIiwiZnVuY3Rpb24gc3ltYm9sKCkgdmlldyByZXR1cm5zIChzdHJpbmcpIiwiZnVuY3Rpb24gZGVjaW1hbHMoKSB2aWV3IHJldHVybnMgKHVpbnQ4KSIsImZ1bmN0aW9uIHRvdGFsU3VwcGx5KCkgdmlldyByZXR1cm5zICh1aW50MjU2KSIsImZ1bmN0aW9uIGJhbGFuY2VPZihhZGRyZXNzKSB2aWV3IHJldHVybnMgKHVpbnQpIiwiZnVuY3Rpb24gdHJhbnNmZXIoYWRkcmVzcyB0bywgdWludCBhbW91bnQpIiwiZnVuY3Rpb24gdHJhbnNmZXJGcm9tKGFkZHJlc3Mgc2VuZGVyLCBhZGRyZXNzIHJlY2lwaWVudCwgdWludDI1NiBhbW91bnQpIGV4dGVybmFsIHJldHVybnMgKGJvb2wpIiwiZnVuY3Rpb24gbWludChhZGRyZXNzIHRvLCB1aW50MjU2IGFtb3VudCkiLCJldmVudCBUcmFuc2ZlcihhZGRyZXNzIGluZGV4ZWQgZnJvbSwgYWRkcmVzcyBpbmRleGVkIHRvLCB1aW50IGFtb3VudCkiLCJldmVudCBBcHByb3ZhbChhZGRyZXNzIGluZGV4ZWQgb3duZXIsIGFkZHJlc3MgaW5kZXhlZCBzcGVuZGVyLCB1aW50MjU2IHZhbHVlKSJd::W10=', 
                address = 0xdac17f958d2ee523a2206206994597c13d831ec7
            )
        else :
            return SmartBchContractResponse(
        )

    def testSmartBchContractResponse(self):
        """Test SmartBchContractResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
