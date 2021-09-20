# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class NetworkEnum(object):
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
        'network': 'str'
    }

    attribute_map = {
        'network': 'network'
    }

    discriminator_value_class_map = {
        'WalletReplaceNamedRequest': 'WalletReplaceNamedRequest',
        'WalletNamedExistsRequest': 'WalletNamedExistsRequest',
        'UtilDecodeTransactionRequest': 'UtilDecodeTransactionRequest',
        'WalletInfo': 'WalletInfo',
        'WalletResponse': 'WalletResponse',
        'SmartBchContractRequest': 'SmartBchContractRequest',
        'ContractRequest': 'ContractRequest',
        'WalletRequest': 'WalletRequest'
    }

    def __init__(self, network=None, local_vars_configuration=None):  # noqa: E501
        """NetworkEnum - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network = None
        self.discriminator = 'network'

        if network is not None:
            self.network = network

    @property
    def network(self):
        """Gets the network of this NetworkEnum.  # noqa: E501

        network type  # noqa: E501

        :return: The network of this NetworkEnum.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this NetworkEnum.

        network type  # noqa: E501

        :param network: The network of this NetworkEnum.  # noqa: E501
        :type network: str
        """
        allowed_values = ["mainnet", "testnet", "regtest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and network not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `network` ({0}), must be one of {1}"  # noqa: E501
                .format(network, allowed_values)
            )

        self._network = network

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
        if not isinstance(other, NetworkEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkEnum):
            return True

        return self.to_dict() != other.to_dict()
