# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.23
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.escrow_request import EscrowRequest  # noqa: E501
from mainnet.rest import ApiException

class TestEscrowRequest(unittest.TestCase):
    """EscrowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EscrowRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.escrow_request.EscrowRequest()  # noqa: E501
        if include_optional :
            return EscrowRequest(
                buyer_addr = bchtest:qrnluuge56ahxsy6pplq43rva7k6s9dknu4p5278ah, 
                arbiter_addr = bchtest:qzspcywxmm4fqhf9kjrknrc3grsv2vukeqyjqla0nt, 
                seller_addr = bchtest:qz00pk9lfs0k9f5vf3j8h66qfmqagk8nc56elq4dv2, 
                amount = 10000
            )
        else :
            return EscrowRequest(
                buyer_addr = bchtest:qrnluuge56ahxsy6pplq43rva7k6s9dknu4p5278ah,
                arbiter_addr = bchtest:qzspcywxmm4fqhf9kjrknrc3grsv2vukeqyjqla0nt,
                seller_addr = bchtest:qz00pk9lfs0k9f5vf3j8h66qfmqagk8nc56elq4dv2,
                amount = 10000,
        )

    def testEscrowRequest(self):
        """Test EscrowRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
