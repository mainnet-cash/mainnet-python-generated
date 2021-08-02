# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.39
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SendRequestItemAnyOf(object):
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
        'cashaddr': 'str',
        'value': 'float'
    }

    attribute_map = {
        'cashaddr': 'cashaddr',
        'value': 'value'
    }

    def __init__(self, cashaddr=None, value=None, local_vars_configuration=None):  # noqa: E501
        """SendRequestItemAnyOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cashaddr = None
        self._value = None
        self.discriminator = None

        self.cashaddr = cashaddr
        self.value = value

    @property
    def cashaddr(self):
        """Gets the cashaddr of this SendRequestItemAnyOf.  # noqa: E501


        :return: The cashaddr of this SendRequestItemAnyOf.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this SendRequestItemAnyOf.


        :param cashaddr: The cashaddr of this SendRequestItemAnyOf.  # noqa: E501
        :type cashaddr: str
        """
        if self.local_vars_configuration.client_side_validation and cashaddr is None:  # noqa: E501
            raise ValueError("Invalid value for `cashaddr`, must not be `None`")  # noqa: E501

        self._cashaddr = cashaddr

    @property
    def value(self):
        """Gets the value of this SendRequestItemAnyOf.  # noqa: E501


        :return: The value of this SendRequestItemAnyOf.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SendRequestItemAnyOf.


        :param value: The value of this SendRequestItemAnyOf.  # noqa: E501
        :type value: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, SendRequestItemAnyOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendRequestItemAnyOf):
            return True

        return self.to_dict() != other.to_dict()
