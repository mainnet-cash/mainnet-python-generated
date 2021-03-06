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
from mainnet.models.slp_genesis_request import SlpGenesisRequest  # noqa: E501
from mainnet.rest import ApiException

class TestSlpGenesisRequest(unittest.TestCase):
    """SlpGenesisRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SlpGenesisRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.slp_genesis_request.SlpGenesisRequest()  # noqa: E501
        if include_optional :
            return SlpGenesisRequest(
                wallet_id = 'wif:testnet:cNfsPtqN2bMRS7vH5qd8tR8GMvgXyL5BjnGAKgZ8DYEiCrCCQcP6', 
                name = 'Mainnet coin', 
                ticker = 'MNC', 
                initial_amount = '10000', 
                decimals = 1.337, 
                document_url = 'https://mainnet.cash', 
                document_hash = 'db4451f11eda33950670aaf59e704da90117ff7057283b032cfaec7779313916', 
                end_baton = False, 
                type = 1, 
                token_receiver_slp_addr = 'slptest:qqm4gsaa2gvk7flvsvj7f0w4rlq32vqhkq32uar866', 
                baton_receiver_slp_addr = 'slptest:qqm4gsaa2gvk7flvsvj7f0w4rlq32vqhkq32uar866', 
                parent_token_id = '132731d90ac4c88a79d55eae2ad92709b415de886329e958cf35fdd81ba34c15'
            )
        else :
            return SlpGenesisRequest(
                wallet_id = 'wif:testnet:cNfsPtqN2bMRS7vH5qd8tR8GMvgXyL5BjnGAKgZ8DYEiCrCCQcP6',
                name = 'Mainnet coin',
                ticker = 'MNC',
                initial_amount = '10000',
                decimals = 1.337,
        )

    def testSlpGenesisRequest(self):
        """Test SlpGenesisRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
