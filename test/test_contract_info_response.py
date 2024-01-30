# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.7
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.contract_info_response import ContractInfoResponse  # noqa: E501
from mainnet.rest import ApiException

class TestContractInfoResponse(unittest.TestCase):
    """ContractInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContractInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.contract_info_response.ContractInfoResponse()  # noqa: E501
        if include_optional :
            return ContractInfoResponse(
                contract_id = '0', 
                script = 'contract TransferWithTimeout(pubkey sender, pubkey recipient, int timeout) {
    function transfer(sig recipientSig) {
        require(checkSig(recipientSig, recipient));
    }

    function timeout(sig senderSig) {
        require(checkSig(senderSig, sender));
        require(tx.time >= timeout);
    }
}
', 
                parameters = ["03410ef048b3da351793f6ed14cc2fde460becc5b658d9138443b9a3000707a6a7","034978ac464f358b235f11212eb6e017af90215b90b1ff7471d9ae2abb5e09263b",215], 
                cashaddr = 'bchtest:qpalhxhl05mlhms3ys43u76rn0ttdv3qg2usm4nm7t', 
                tokenaddr = 'bchreg:zpttdv3qg2usm4nm7talhxhl05mlhms3ysjm0q59vu'
            )
        else :
            return ContractInfoResponse(
        )

    def testContractInfoResponse(self):
        """Test ContractInfoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
