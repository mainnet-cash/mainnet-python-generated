# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.19
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class UtilDecodeTransactionRequest(object):
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
        'transaction_hash_or_hex': 'str',
        'load_input_values': 'bool'
    }

    attribute_map = {
        'transaction_hash_or_hex': 'transactionHashOrHex',
        'load_input_values': 'loadInputValues'
    }

    def __init__(self, transaction_hash_or_hex=None, load_input_values=None, local_vars_configuration=None):  # noqa: E501
        """UtilDecodeTransactionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._transaction_hash_or_hex = None
        self._load_input_values = None
        self.discriminator = None

        self.transaction_hash_or_hex = transaction_hash_or_hex
        if load_input_values is not None:
            self.load_input_values = load_input_values

    @property
    def transaction_hash_or_hex(self):
        """Gets the transaction_hash_or_hex of this UtilDecodeTransactionRequest.  # noqa: E501


        :return: The transaction_hash_or_hex of this UtilDecodeTransactionRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash_or_hex

    @transaction_hash_or_hex.setter
    def transaction_hash_or_hex(self, transaction_hash_or_hex):
        """Sets the transaction_hash_or_hex of this UtilDecodeTransactionRequest.


        :param transaction_hash_or_hex: The transaction_hash_or_hex of this UtilDecodeTransactionRequest.  # noqa: E501
        :type transaction_hash_or_hex: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_hash_or_hex is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_hash_or_hex`, must not be `None`")  # noqa: E501

        self._transaction_hash_or_hex = transaction_hash_or_hex

    @property
    def load_input_values(self):
        """Gets the load_input_values of this UtilDecodeTransactionRequest.  # noqa: E501

        A flag whether to load or not extra information about transaction inputs (cashaddress and value)  # noqa: E501

        :return: The load_input_values of this UtilDecodeTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._load_input_values

    @load_input_values.setter
    def load_input_values(self, load_input_values):
        """Sets the load_input_values of this UtilDecodeTransactionRequest.

        A flag whether to load or not extra information about transaction inputs (cashaddress and value)  # noqa: E501

        :param load_input_values: The load_input_values of this UtilDecodeTransactionRequest.  # noqa: E501
        :type load_input_values: bool
        """

        self._load_input_values = load_input_values

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
        if not isinstance(other, UtilDecodeTransactionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UtilDecodeTransactionRequest):
            return True

        return self.to_dict() != other.to_dict()
