# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.21
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchOverrides(object):
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
        'gas_limit': 'AnyOfnumberstring',
        'gas_price': 'AnyOfnumberstring',
        'max_fee_per_gas': 'AnyOfnumberstring',
        'max_priority_fee_per_gas': 'AnyOfnumberstring',
        'nonce': 'AnyOfnumberstring',
        'value': 'AnyOfnumberstring',
        'block_tag': 'AnyOfnumberstring',
        '_from': 'str'
    }

    attribute_map = {
        'gas_limit': 'gasLimit',
        'gas_price': 'gasPrice',
        'max_fee_per_gas': 'maxFeePerGas',
        'max_priority_fee_per_gas': 'maxPriorityFeePerGas',
        'nonce': 'nonce',
        'value': 'value',
        'block_tag': 'blockTag',
        '_from': 'from'
    }

    def __init__(self, gas_limit=None, gas_price=None, max_fee_per_gas=None, max_priority_fee_per_gas=None, nonce=None, value=None, block_tag=None, _from=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchOverrides - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gas_limit = None
        self._gas_price = None
        self._max_fee_per_gas = None
        self._max_priority_fee_per_gas = None
        self._nonce = None
        self._value = None
        self._block_tag = None
        self.__from = None
        self.discriminator = None

        if gas_limit is not None:
            self.gas_limit = gas_limit
        if gas_price is not None:
            self.gas_price = gas_price
        if max_fee_per_gas is not None:
            self.max_fee_per_gas = max_fee_per_gas
        if max_priority_fee_per_gas is not None:
            self.max_priority_fee_per_gas = max_priority_fee_per_gas
        if nonce is not None:
            self.nonce = nonce
        if value is not None:
            self.value = value
        if block_tag is not None:
            self.block_tag = block_tag
        if _from is not None:
            self._from = _from

    @property
    def gas_limit(self):
        """Gets the gas_limit of this SmartBchOverrides.  # noqa: E501


        :return: The gas_limit of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._gas_limit

    @gas_limit.setter
    def gas_limit(self, gas_limit):
        """Sets the gas_limit of this SmartBchOverrides.


        :param gas_limit: The gas_limit of this SmartBchOverrides.  # noqa: E501
        :type gas_limit: AnyOfnumberstring
        """

        self._gas_limit = gas_limit

    @property
    def gas_price(self):
        """Gets the gas_price of this SmartBchOverrides.  # noqa: E501


        :return: The gas_price of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._gas_price

    @gas_price.setter
    def gas_price(self, gas_price):
        """Sets the gas_price of this SmartBchOverrides.


        :param gas_price: The gas_price of this SmartBchOverrides.  # noqa: E501
        :type gas_price: AnyOfnumberstring
        """

        self._gas_price = gas_price

    @property
    def max_fee_per_gas(self):
        """Gets the max_fee_per_gas of this SmartBchOverrides.  # noqa: E501


        :return: The max_fee_per_gas of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._max_fee_per_gas

    @max_fee_per_gas.setter
    def max_fee_per_gas(self, max_fee_per_gas):
        """Sets the max_fee_per_gas of this SmartBchOverrides.


        :param max_fee_per_gas: The max_fee_per_gas of this SmartBchOverrides.  # noqa: E501
        :type max_fee_per_gas: AnyOfnumberstring
        """

        self._max_fee_per_gas = max_fee_per_gas

    @property
    def max_priority_fee_per_gas(self):
        """Gets the max_priority_fee_per_gas of this SmartBchOverrides.  # noqa: E501


        :return: The max_priority_fee_per_gas of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._max_priority_fee_per_gas

    @max_priority_fee_per_gas.setter
    def max_priority_fee_per_gas(self, max_priority_fee_per_gas):
        """Sets the max_priority_fee_per_gas of this SmartBchOverrides.


        :param max_priority_fee_per_gas: The max_priority_fee_per_gas of this SmartBchOverrides.  # noqa: E501
        :type max_priority_fee_per_gas: AnyOfnumberstring
        """

        self._max_priority_fee_per_gas = max_priority_fee_per_gas

    @property
    def nonce(self):
        """Gets the nonce of this SmartBchOverrides.  # noqa: E501


        :return: The nonce of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this SmartBchOverrides.


        :param nonce: The nonce of this SmartBchOverrides.  # noqa: E501
        :type nonce: AnyOfnumberstring
        """

        self._nonce = nonce

    @property
    def value(self):
        """Gets the value of this SmartBchOverrides.  # noqa: E501


        :return: The value of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SmartBchOverrides.


        :param value: The value of this SmartBchOverrides.  # noqa: E501
        :type value: AnyOfnumberstring
        """

        self._value = value

    @property
    def block_tag(self):
        """Gets the block_tag of this SmartBchOverrides.  # noqa: E501


        :return: The block_tag of this SmartBchOverrides.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._block_tag

    @block_tag.setter
    def block_tag(self, block_tag):
        """Sets the block_tag of this SmartBchOverrides.


        :param block_tag: The block_tag of this SmartBchOverrides.  # noqa: E501
        :type block_tag: AnyOfnumberstring
        """

        self._block_tag = block_tag

    @property
    def _from(self):
        """Gets the _from of this SmartBchOverrides.  # noqa: E501


        :return: The _from of this SmartBchOverrides.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SmartBchOverrides.


        :param _from: The _from of this SmartBchOverrides.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

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
        if not isinstance(other, SmartBchOverrides):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchOverrides):
            return True

        return self.to_dict() != other.to_dict()
