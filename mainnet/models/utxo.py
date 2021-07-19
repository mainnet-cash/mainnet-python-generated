# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.30
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class Utxo(object):
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
        'index': 'float',
        'tx_id': 'str',
        'value': 'float',
        'utxo_id': 'str'
    }

    attribute_map = {
        'index': 'index',
        'tx_id': 'txId',
        'value': 'value',
        'utxo_id': 'utxoId'
    }

    def __init__(self, index=None, tx_id=None, value=None, utxo_id=None, local_vars_configuration=None):  # noqa: E501
        """Utxo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._tx_id = None
        self._value = None
        self._utxo_id = None
        self.discriminator = None

        if index is not None:
            self.index = index
        self.tx_id = tx_id
        self.value = value
        self.utxo_id = utxo_id

    @property
    def index(self):
        """Gets the index of this Utxo.  # noqa: E501


        :return: The index of this Utxo.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this Utxo.


        :param index: The index of this Utxo.  # noqa: E501
        :type index: float
        """

        self._index = index

    @property
    def tx_id(self):
        """Gets the tx_id of this Utxo.  # noqa: E501

        The hash of a transaction  # noqa: E501

        :return: The tx_id of this Utxo.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this Utxo.

        The hash of a transaction  # noqa: E501

        :param tx_id: The tx_id of this Utxo.  # noqa: E501
        :type tx_id: str
        """
        if self.local_vars_configuration.client_side_validation and tx_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tx_id`, must not be `None`")  # noqa: E501

        self._tx_id = tx_id

    @property
    def value(self):
        """Gets the value of this Utxo.  # noqa: E501


        :return: The value of this Utxo.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Utxo.


        :param value: The value of this Utxo.  # noqa: E501
        :type value: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def utxo_id(self):
        """Gets the utxo_id of this Utxo.  # noqa: E501

        serialized outpoint  # noqa: E501

        :return: The utxo_id of this Utxo.  # noqa: E501
        :rtype: str
        """
        return self._utxo_id

    @utxo_id.setter
    def utxo_id(self, utxo_id):
        """Sets the utxo_id of this Utxo.

        serialized outpoint  # noqa: E501

        :param utxo_id: The utxo_id of this Utxo.  # noqa: E501
        :type utxo_id: str
        """
        if self.local_vars_configuration.client_side_validation and utxo_id is None:  # noqa: E501
            raise ValueError("Invalid value for `utxo_id`, must not be `None`")  # noqa: E501

        self._utxo_id = utxo_id

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
        if not isinstance(other, Utxo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Utxo):
            return True

        return self.to_dict() != other.to_dict()
