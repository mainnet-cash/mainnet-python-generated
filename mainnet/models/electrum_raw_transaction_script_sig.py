# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.6.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ElectrumRawTransactionScriptSig(object):
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
        'asm': 'str',
        'hex': 'str'
    }

    attribute_map = {
        'asm': 'asm',
        'hex': 'hex'
    }

    def __init__(self, asm=None, hex=None, local_vars_configuration=None):  # noqa: E501
        """ElectrumRawTransactionScriptSig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asm = None
        self._hex = None
        self.discriminator = None

        if asm is not None:
            self.asm = asm
        if hex is not None:
            self.hex = hex

    @property
    def asm(self):
        """Gets the asm of this ElectrumRawTransactionScriptSig.  # noqa: E501


        :return: The asm of this ElectrumRawTransactionScriptSig.  # noqa: E501
        :rtype: str
        """
        return self._asm

    @asm.setter
    def asm(self, asm):
        """Sets the asm of this ElectrumRawTransactionScriptSig.


        :param asm: The asm of this ElectrumRawTransactionScriptSig.  # noqa: E501
        :type asm: str
        """

        self._asm = asm

    @property
    def hex(self):
        """Gets the hex of this ElectrumRawTransactionScriptSig.  # noqa: E501


        :return: The hex of this ElectrumRawTransactionScriptSig.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this ElectrumRawTransactionScriptSig.


        :param hex: The hex of this ElectrumRawTransactionScriptSig.  # noqa: E501
        :type hex: str
        """

        self._hex = hex

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
        if not isinstance(other, ElectrumRawTransactionScriptSig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectrumRawTransactionScriptSig):
            return True

        return self.to_dict() != other.to_dict()
