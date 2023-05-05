# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class CashscriptReceipt(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'to': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'to': 'to',
        'amount': 'amount'
    }

    def __init__(self, to=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """CashscriptReceipt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._amount = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if amount is not None:
            self.amount = amount

    @property
    def to(self):
        """Gets the to of this CashscriptReceipt.  # noqa: E501


        :return: The to of this CashscriptReceipt.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this CashscriptReceipt.


        :param to: The to of this CashscriptReceipt.  # noqa: E501
        :type to: str
        """

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this CashscriptReceipt.  # noqa: E501


        :return: The amount of this CashscriptReceipt.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CashscriptReceipt.


        :param amount: The amount of this CashscriptReceipt.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CashscriptReceipt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CashscriptReceipt):
            return True

        return self.to_dict() != other.to_dict()
