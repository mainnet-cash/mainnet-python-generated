# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.5.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.smart_bch_contract_deploy_request import SmartBchContractDeployRequest  # noqa: E501
from mainnet.rest import ApiException

class TestSmartBchContractDeployRequest(unittest.TestCase):
    """SmartBchContractDeployRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SmartBchContractDeployRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.smart_bch_contract_deploy_request.SmartBchContractDeployRequest()  # noqa: E501
        if include_optional :
            return SmartBchContractDeployRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45', 
                script = '// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/SEP20/SEP20.sol";

contract MyToken is SEP20 {
  constructor(string memory name, string memory symbol) SEP20(name, symbol) {}
}
', 
                parameters = ["MyToken","MTK"], 
                overrides = mainnet.models.smart_bch_overrides.SmartBchOverrides(
                    gas_limit = null, 
                    gas_price = null, 
                    max_fee_per_gas = null, 
                    max_priority_fee_per_gas = null, 
                    nonce = null, 
                    value = null, 
                    block_tag = null, 
                    from = '0', )
            )
        else :
            return SmartBchContractDeployRequest(
                wallet_id = 'privkey:regtest:0x758c7be51a76a9b6bc6b3e1a90e5ff4cc27aa054b77b7acb6f4f08a219c1ce45',
                script = '// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/SEP20/SEP20.sol";

contract MyToken is SEP20 {
  constructor(string memory name, string memory symbol) SEP20(name, symbol) {}
}
',
        )

    def testSmartBchContractDeployRequest(self):
        """Test SmartBchContractDeployRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
