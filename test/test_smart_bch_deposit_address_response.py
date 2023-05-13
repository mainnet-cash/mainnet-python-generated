# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_deposit_address_response import SmartBchDepositAddressResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchDepositAddressResponse(unittest.TestCase):
    """SmartBchDepositAddressResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchDepositAddressResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_deposit_address_response.SmartBchDepositAddressResponse()  # noqa: E501
        if include_optional :
            return SmartBchDepositAddressResponse(
                address = '0xE25ddbAF8DD61b627727e03e190E32feddBD1319'
            )
        else :
            return SmartBchDepositAddressResponse(
        )

    def testSmartBchDepositAddressResponse(self):
        """Test SmartBchDepositAddressResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
