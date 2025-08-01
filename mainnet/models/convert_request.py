# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.7.14
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ConvertRequest(object):
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
        'value': 'float',
        '_from': 'str',
        'to': 'str'
    }

    attribute_map = {
        'value': 'value',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, value=None, _from=None, to=None, local_vars_configuration=None):  # noqa: E501
        """ConvertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.value = value
        self._from = _from
        self.to = to

    @property
    def value(self):
        """Gets the value of this ConvertRequest.  # noqa: E501


        :return: The value of this ConvertRequest.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConvertRequest.


        :param value: The value of this ConvertRequest.  # noqa: E501
        :type value: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def _from(self):
        """Gets the _from of this ConvertRequest.  # noqa: E501

        Provided value unit of account.  # noqa: E501

        :return: The _from of this ConvertRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ConvertRequest.

        Provided value unit of account.  # noqa: E501

        :param _from: The _from of this ConvertRequest.  # noqa: E501
        :type _from: str
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501
        allowed_values = ["bch", "BCH", "usd", "USD", "bit", "bits", "sat", "SAT", "sats", "satoshi", "satoshis"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and _from not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `_from` ({0}), must be one of {1}"  # noqa: E501
                .format(_from, allowed_values)
            )

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ConvertRequest.  # noqa: E501

        Unit of account to be returned  # noqa: E501

        :return: The to of this ConvertRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ConvertRequest.

        Unit of account to be returned  # noqa: E501

        :param to: The to of this ConvertRequest.  # noqa: E501
        :type to: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501
        allowed_values = ["bch", "BCH", "usd", "USD", "bit", "bits", "sat", "SAT", "sats", "satoshi", "satoshis"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and to not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `to` ({0}), must be one of {1}"  # noqa: E501
                .format(to, allowed_values)
            )

        self._to = to

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
        if not isinstance(other, ConvertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertRequest):
            return True

        return self.to_dict() != other.to_dict()
