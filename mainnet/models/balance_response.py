# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.12
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class BalanceResponse(object):
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
        'bch': 'float',
        'sat': 'int',
        'usd': 'float'
    }

    attribute_map = {
        'bch': 'bch',
        'sat': 'sat',
        'usd': 'usd'
    }

    def __init__(self, bch=None, sat=None, usd=None, local_vars_configuration=None):  # noqa: E501
        """BalanceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bch = None
        self._sat = None
        self._usd = None
        self.discriminator = None

        if bch is not None:
            self.bch = bch
        if sat is not None:
            self.sat = sat
        if usd is not None:
            self.usd = usd

    @property
    def bch(self):
        """Gets the bch of this BalanceResponse.  # noqa: E501

        Amount in whole Bitcoin Cash  # noqa: E501

        :return: The bch of this BalanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._bch

    @bch.setter
    def bch(self, bch):
        """Sets the bch of this BalanceResponse.

        Amount in whole Bitcoin Cash  # noqa: E501

        :param bch: The bch of this BalanceResponse.  # noqa: E501
        :type bch: float
        """

        self._bch = bch

    @property
    def sat(self):
        """Gets the sat of this BalanceResponse.  # noqa: E501

        Amount in satoshis  # noqa: E501

        :return: The sat of this BalanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._sat

    @sat.setter
    def sat(self, sat):
        """Sets the sat of this BalanceResponse.

        Amount in satoshis  # noqa: E501

        :param sat: The sat of this BalanceResponse.  # noqa: E501
        :type sat: int
        """

        self._sat = sat

    @property
    def usd(self):
        """Gets the usd of this BalanceResponse.  # noqa: E501

        Amount in United States Dollars  # noqa: E501

        :return: The usd of this BalanceResponse.  # noqa: E501
        :rtype: float
        """
        return self._usd

    @usd.setter
    def usd(self, usd):
        """Sets the usd of this BalanceResponse.

        Amount in United States Dollars  # noqa: E501

        :param usd: The usd of this BalanceResponse.  # noqa: E501
        :type usd: float
        """

        self._usd = usd

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
        if not isinstance(other, BalanceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BalanceResponse):
            return True

        return self.to_dict() != other.to_dict()
