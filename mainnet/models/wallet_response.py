# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.13
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class WalletResponse(object):
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
        'wallet_id': 'str',
        'name': 'str',
        'cashaddr': 'str',
        'slpaddr': 'str'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'name': 'name',
        'cashaddr': 'cashaddr',
        'slpaddr': 'slpaddr'
    }

    def __init__(self, wallet_id=None, name=None, cashaddr=None, slpaddr=None, local_vars_configuration=None):  # noqa: E501
        """WalletResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._name = None
        self._cashaddr = None
        self._slpaddr = None
        self.discriminator = None

        if wallet_id is not None:
            self.wallet_id = wallet_id
        if name is not None:
            self.name = name
        if cashaddr is not None:
            self.cashaddr = cashaddr
        if slpaddr is not None:
            self.slpaddr = slpaddr

    @property
    def wallet_id(self):
        """Gets the wallet_id of this WalletResponse.  # noqa: E501

        All the information necessary to reconstruct a wallet, including private information, type and network.   # noqa: E501

        :return: The wallet_id of this WalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this WalletResponse.

        All the information necessary to reconstruct a wallet, including private information, type and network.   # noqa: E501

        :param wallet_id: The wallet_id of this WalletResponse.  # noqa: E501
        :type wallet_id: str
        """

        self._wallet_id = wallet_id

    @property
    def name(self):
        """Gets the name of this WalletResponse.  # noqa: E501

        User defined string for wallet  # noqa: E501

        :return: The name of this WalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WalletResponse.

        User defined string for wallet  # noqa: E501

        :param name: The name of this WalletResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def cashaddr(self):
        """Gets the cashaddr of this WalletResponse.  # noqa: E501

        The address in cashaddr format.   # noqa: E501

        :return: The cashaddr of this WalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this WalletResponse.

        The address in cashaddr format.   # noqa: E501

        :param cashaddr: The cashaddr of this WalletResponse.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def slpaddr(self):
        """Gets the slpaddr of this WalletResponse.  # noqa: E501

        The SLP address of the wallet in cashaddr format.   # noqa: E501

        :return: The slpaddr of this WalletResponse.  # noqa: E501
        :rtype: str
        """
        return self._slpaddr

    @slpaddr.setter
    def slpaddr(self, slpaddr):
        """Sets the slpaddr of this WalletResponse.

        The SLP address of the wallet in cashaddr format.   # noqa: E501

        :param slpaddr: The slpaddr of this WalletResponse.  # noqa: E501
        :type slpaddr: str
        """

        self._slpaddr = slpaddr

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
        if not isinstance(other, WalletResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletResponse):
            return True

        return self.to_dict() != other.to_dict()
