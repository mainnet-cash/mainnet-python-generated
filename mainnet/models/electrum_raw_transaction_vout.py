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


class ElectrumRawTransactionVout(object):
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
        'n': 'float',
        'script_pub_key': 'ElectrumRawTransactionScriptPubKey',
        'value': 'float'
    }

    attribute_map = {
        'n': 'n',
        'script_pub_key': 'scriptPubKey',
        'value': 'value'
    }

    def __init__(self, n=None, script_pub_key=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ElectrumRawTransactionVout - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._n = None
        self._script_pub_key = None
        self._value = None
        self.discriminator = None

        if n is not None:
            self.n = n
        if script_pub_key is not None:
            self.script_pub_key = script_pub_key
        if value is not None:
            self.value = value

    @property
    def n(self):
        """Gets the n of this ElectrumRawTransactionVout.  # noqa: E501


        :return: The n of this ElectrumRawTransactionVout.  # noqa: E501
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this ElectrumRawTransactionVout.


        :param n: The n of this ElectrumRawTransactionVout.  # noqa: E501
        :type n: float
        """

        self._n = n

    @property
    def script_pub_key(self):
        """Gets the script_pub_key of this ElectrumRawTransactionVout.  # noqa: E501


        :return: The script_pub_key of this ElectrumRawTransactionVout.  # noqa: E501
        :rtype: ElectrumRawTransactionScriptPubKey
        """
        return self._script_pub_key

    @script_pub_key.setter
    def script_pub_key(self, script_pub_key):
        """Sets the script_pub_key of this ElectrumRawTransactionVout.


        :param script_pub_key: The script_pub_key of this ElectrumRawTransactionVout.  # noqa: E501
        :type script_pub_key: ElectrumRawTransactionScriptPubKey
        """

        self._script_pub_key = script_pub_key

    @property
    def value(self):
        """Gets the value of this ElectrumRawTransactionVout.  # noqa: E501


        :return: The value of this ElectrumRawTransactionVout.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ElectrumRawTransactionVout.


        :param value: The value of this ElectrumRawTransactionVout.  # noqa: E501
        :type value: float
        """

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
        if not isinstance(other, ElectrumRawTransactionVout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectrumRawTransactionVout):
            return True

        return self.to_dict() != other.to_dict()
