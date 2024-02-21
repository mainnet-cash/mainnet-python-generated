# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.10
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.escrow_info_response import EscrowInfoResponse  # noqa: E501
from mainnet.rest import ApiException

class TestEscrowInfoResponse(unittest.TestCase):
    """EscrowInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EscrowInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.escrow_info_response.EscrowInfoResponse()  # noqa: E501
        if include_optional :
            return EscrowInfoResponse(
                escrow_contract_id = 'escrowContract:testnet:WW1Ob2RHVnpkRHB4ZWpBd2NHczViR1p6TUdzNVpqVjJaak5xT0dnMk5uRm1iWEZoWjJzNGJtTTFObVZzY1RSa2RqST06WW1Ob2RHVnpkRHB4Y201c2RYVm5aVFUyWVdoNGMzazJjSEJzY1RRemNuWmhOMnMyY3psa2EyNTFOSEExTWpjNFlXZz06WW1Ob2RHVnpkRHB4ZW5Od1kzbDNlRzF0TkdaeGFHWTVhMnB5YTI1eVl6Tm5jbk4yTW5aMWEyVnhlV3B4YkdFd2JuUT06TVRBd01EQT0=:TVRVNExESTBNQ3d5TVRZc01Ua3hMRGMyTERNeExEazRMREUyTml3eE5EQXNOellzTVRBd0xERXlNeXd5TXpVc05qUXNOemdzTVRrekxESXhNaXc0T0N3eU5ETXNNVGszOk1qTXhMREkxTkN3eE1UTXNNalVzTVRZMkxERTROeXd4TVRVc05qUXNNVFUwTERnc01USTJMREV3TERFNU5pd3hNRGdzTWpNNUxERTNNeXd4Tmpnc01qRXNNVGd5TERFMU9RPT06TVRZd0xESTRMREUzTERFNU9Dd3lNaklzTWpNMExERTBOQ3c1TXl3ek55d3hPREFzTVRNMUxERXdOU3d4TkRNc01UY3NOalFzTWpJMExERTVOeXcxTVN3eE5UQXNNakF3Ok1UQXdNREE9Ok1UQTNOVEU0TkRjeU53PT0=:cHJhZ21hIGNhc2hzY3JpcHQgXjAuNi4xOwogICAgICAgICAgICBjb250cmFjdCBlc2Nyb3coYnl0ZXMyMCBzZWxsZXJQa2gsIGJ5dGVzMjAgYnV5ZXJQa2gsIGJ5dGVzMjAgYXJiaXRlclBraCwgaW50IGNvbnRyYWN0QW1vdW50LCBpbnQgY29udHJhY3ROb25jZSkgewoKICAgICAgICAgICAgICAgIGZ1bmN0aW9uIHNwZW5kKHB1YmtleSBzaWduaW5nUGssIHNpZyBzLCBpbnQgYW1vdW50LCBpbnQgbm9uY2UpIHsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBhcmJpdGVyUGtoIHx8IGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBidXllclBraCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShjaGVja1NpZyhzLCBzaWduaW5nUGspKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGFtb3VudCA+PSBjb250cmFjdEFtb3VudCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShub25jZSA9PSBjb250cmFjdE5vbmNlKTsKICAgICAgICAgICAgICAgICAgICBieXRlczM0IG91dHB1dCA9IG5ldyBPdXRwdXRQMlBLSChieXRlczgoYW1vdW50KSwgc2VsbGVyUGtoKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gyNTYob3V0cHV0KSA9PSB0eC5oYXNoT3V0cHV0cyk7CiAgICAgICAgICAgICAgICB9CgogICAgICAgICAgICAgICAgZnVuY3Rpb24gcmVmdW5kKHB1YmtleSBzaWduaW5nUGssIHNpZyBzLCBpbnQgYW1vdW50LCBpbnQgbm9uY2UpIHsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBhcmJpdGVyUGtofHxoYXNoMTYwKHNpZ25pbmdQaykgPT0gc2VsbGVyUGtoKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGNoZWNrU2lnKHMsIHNpZ25pbmdQaykpOwogICAgICAgICAgICAgICAgICAgIHJlcXVpcmUoYW1vdW50ID49IGNvbnRyYWN0QW1vdW50KTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKG5vbmNlID09IGNvbnRyYWN0Tm9uY2UpOwogICAgICAgICAgICAgICAgICAgIGJ5dGVzMzQgb3V0cHV0ID0gbmV3IE91dHB1dFAyUEtIKGJ5dGVzOChhbW91bnQpLCBidXllclBraCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShoYXNoMjU2KG91dHB1dCkgPT0gdHguaGFzaE91dHB1dHMpOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAg:1075184727', 
                script = 'pragma cashscript ^0.6.1;
contract escrow(bytes20 sellerPkh, bytes20 buyerPkh, bytes20 arbiterPkh, int contractAmount, int contractNonce) {

    function spend(pubkey signingPk, sig s, int amount, int nonce) {
        require(hash160(signingPk) == arbiterPkh || hash160(signingPk) == buyerPkh);
        require(checkSig(s, signingPk));
        require(amount >= contractAmount);
        require(nonce == contractNonce);
        bytes34 output = new OutputP2PKH(bytes8(amount), sellerPkh);
        require(hash256(output) == tx.hashOutputs);
    }

    function refund(pubkey signingPk, sig s, int amount, int nonce) {
        require(hash160(signingPk) == arbiterPkh||hash160(signingPk) == sellerPkh);
        require(checkSig(s, signingPk));
        require(amount >= contractAmount);
        require(nonce == contractNonce);
        bytes34 output = new OutputP2PKH(bytes8(amount), buyerPkh);
        require(hash256(output) == tx.hashOutputs);
    }
}
', 
                parameters = ["9ef0d8bf4c1f62a68c4c647beb404ec1d458f3c5","e7fe7119a6bb73409a087e0ac46cefada815b69f","a01c11c6deea905d25b487698f1140e0c53396c8",10000,1996128042], 
                cashaddr = 'bchtest:prxla49zwqm8m2nzgn82qza3ssrqnpt8vgv60hlwm2', 
                buyer_addr = bchtest:qrnluuge56ahxsy6pplq43rva7k6s9dknu4p5278ah, 
                arbiter_addr = bchtest:qzspcywxmm4fqhf9kjrknrc3grsv2vukeqyjqla0nt, 
                seller_addr = bchtest:qz00pk9lfs0k9f5vf3j8h66qfmqagk8nc56elq4dv2, 
                amount = 10000, 
                nonce = 1996128042
            )
        else :
            return EscrowInfoResponse(
        )

    def testEscrowInfoResponse(self):
        """Test EscrowInfoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
