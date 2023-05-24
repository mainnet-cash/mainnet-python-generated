# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.24
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class WalletMnemonic(object):
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
        'seed': 'str',
        'derivation_path': 'str'
    }

    attribute_map = {
        'seed': 'seed',
        'derivation_path': 'derivationPath'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, seed=None, derivation_path=None, local_vars_configuration=None):  # noqa: E501
        """WalletMnemonic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._seed = None
        self._derivation_path = None
        self.discriminator = 'seed'

        if seed is not None:
            self.seed = seed
        if derivation_path is not None:
            self.derivation_path = derivation_path

    @property
    def seed(self):
        """Gets the seed of this WalletMnemonic.  # noqa: E501


        :return: The seed of this WalletMnemonic.  # noqa: E501
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this WalletMnemonic.


        :param seed: The seed of this WalletMnemonic.  # noqa: E501
        :type seed: str
        """

        self._seed = seed

    @property
    def derivation_path(self):
        """Gets the derivation_path of this WalletMnemonic.  # noqa: E501


        :return: The derivation_path of this WalletMnemonic.  # noqa: E501
        :rtype: str
        """
        return self._derivation_path

    @derivation_path.setter
    def derivation_path(self, derivation_path):
        """Sets the derivation_path of this WalletMnemonic.


        :param derivation_path: The derivation_path of this WalletMnemonic.  # noqa: E501
        :type derivation_path: str
        """

        self._derivation_path = derivation_path

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, WalletMnemonic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletMnemonic):
            return True

        return self.to_dict() != other.to_dict()
