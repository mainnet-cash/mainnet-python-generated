# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.11
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class EncodeTransactionResponse(object):
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
        'transaction_hex': 'str'
    }

    attribute_map = {
        'transaction_hex': 'transactionHex'
    }

    def __init__(self, transaction_hex=None, local_vars_configuration=None):  # noqa: E501
        """EncodeTransactionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_hex = None
        self.discriminator = None

        self.transaction_hex = transaction_hex

    @property
    def transaction_hex(self):
        """Gets the transaction_hex of this EncodeTransactionResponse.  # noqa: E501

        encoded transaction in hex format  # noqa: E501

        :return: The transaction_hex of this EncodeTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hex

    @transaction_hex.setter
    def transaction_hex(self, transaction_hex):
        """Sets the transaction_hex of this EncodeTransactionResponse.

        encoded transaction in hex format  # noqa: E501

        :param transaction_hex: The transaction_hex of this EncodeTransactionResponse.  # noqa: E501
        :type transaction_hex: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_hex is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_hex`, must not be `None`")  # noqa: E501

        self._transaction_hex = transaction_hex

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
        if not isinstance(other, EncodeTransactionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EncodeTransactionResponse):
            return True

        return self.to_dict() != other.to_dict()
