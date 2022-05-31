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
from mainnet.models.smart_bch_contract_info_response import SmartBchContractInfoResponse  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchContractInfoResponse(unittest.TestCase):
    """SmartBchContractInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchContractInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_contract_info_response.SmartBchContractInfoResponse()  # noqa: E501
        if include_optional :
            return SmartBchContractInfoResponse(
                contract_id = '0', 
                address = '0', 
                abi = - "function name() view returns (string)"
- "function symbol() view returns (string)"
, 
                script = '// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/SEP20/SEP20.sol";

contract MyToken is SEP20 {
  constructor(string memory name, string memory symbol) SEP20(name, symbol) {}
}
', 
                parameters = ["MyToken","MTK"]
            )
        else :
            return SmartBchContractInfoResponse(
        )

    def testSmartBchContractInfoResponse(self):
        """Test SmartBchContractInfoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
