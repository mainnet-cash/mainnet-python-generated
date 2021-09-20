# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.electrum_raw_transaction import ElectrumRawTransaction  # noqa: E501
from mainnet.rest import ApiException

class TestElectrumRawTransaction(unittest.TestCase):
    """ElectrumRawTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ElectrumRawTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.electrum_raw_transaction.ElectrumRawTransaction()  # noqa: E501
        if include_optional :
            return ElectrumRawTransaction(
                blockhash = '0', 
                blocktime = 1.337, 
                confirmations = 1.337, 
                hash = '0', 
                hex = '0', 
                locktime = 1.337, 
                size = 1.337, 
                time = 1.337, 
                txid = '0', 
                version = 1.337, 
                vin = [
                    mainnet.models.electrum_raw_transaction_vin.ElectrumRawTransaction_vin(
                        script_sig = mainnet.models.electrum_raw_transaction_script_sig.ElectrumRawTransaction_scriptSig(
                            asm = '0', 
                            hex = '0', ), 
                        sequence = 1.337, 
                        txid = '0', 
                        vout = 1.337, 
                        value = 1.337, 
                        address = '0', )
                    ], 
                vout = [
                    mainnet.models.electrum_raw_transaction_vout.ElectrumRawTransaction_vout(
                        n = 1.337, 
                        script_pub_key = mainnet.models.electrum_raw_transaction_script_pub_key.ElectrumRawTransaction_scriptPubKey(
                            addresses = [
                                '0'
                                ], 
                            asm = '0', 
                            hex = '0', 
                            req_sigs = 1.337, 
                            type = '0', ), 
                        value = 1.337, )
                    ]
            )
        else :
            return ElectrumRawTransaction(
        )

    def testElectrumRawTransaction(self):
        """Test ElectrumRawTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
