# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.24
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mainnet
from mainnet.models.scalable_vector_graphic import ScalableVectorGraphic  # noqa: E501
from mainnet.rest import ApiException

class TestScalableVectorGraphic(unittest.TestCase):
    """ScalableVectorGraphic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScalableVectorGraphic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mainnet.models.scalable_vector_graphic.ScalableVectorGraphic()  # noqa: E501
        if include_optional :
            return ScalableVectorGraphic(
                src = 'data:image/svg+xml;base64,PD94bWwgdm... ==**', 
                title = 'bitcoincash:qpttdv3qg2usm4nm7talhxhl05mlhms3ys43u76rn0', 
                alt = 'A Bitcoin Cash Qr Code'
            )
        else :
            return ScalableVectorGraphic(
        )

    def testScalableVectorGraphic(self):
        """Test ScalableVectorGraphic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
