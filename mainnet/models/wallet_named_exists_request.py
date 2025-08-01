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


class WalletNamedExistsRequest(object):
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
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, name=None, type=None, local_vars_configuration=None):  # noqa: E501
        """WalletNamedExistsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this WalletNamedExistsRequest.  # noqa: E501

        User friendly wallet alias  # noqa: E501

        :return: The name of this WalletNamedExistsRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WalletNamedExistsRequest.

        User friendly wallet alias  # noqa: E501

        :param name: The name of this WalletNamedExistsRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this WalletNamedExistsRequest.  # noqa: E501

        Wallet type, either a mnemonic seed single address wallet, a simple private key (wif) or a *Hierarchical Deterministic wallet determined from a seed (not yet implemented)* .  # noqa: E501

        :return: The type of this WalletNamedExistsRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WalletNamedExistsRequest.

        Wallet type, either a mnemonic seed single address wallet, a simple private key (wif) or a *Hierarchical Deterministic wallet determined from a seed (not yet implemented)* .  # noqa: E501

        :param type: The type of this WalletNamedExistsRequest.  # noqa: E501
        :type type: str
        """
        allowed_values = ["wif", "hd", "seed", "watch", "privkey"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, WalletNamedExistsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletNamedExistsRequest):
            return True

        return self.to_dict() != other.to_dict()
