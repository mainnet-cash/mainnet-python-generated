# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class TokenMintRequestRequests(object):
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
        'capability': 'str',
        'commitment': 'str',
        'cashaddr': 'str',
        'value': 'float'
    }

    attribute_map = {
        'capability': 'capability',
        'commitment': 'commitment',
        'cashaddr': 'cashaddr',
        'value': 'value'
    }

    def __init__(self, capability=None, commitment=None, cashaddr=None, value=1000, local_vars_configuration=None):  # noqa: E501
        """TokenMintRequestRequests - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capability = None
        self._commitment = None
        self._cashaddr = None
        self._value = None
        self.discriminator = None

        if capability is not None:
            self.capability = capability
        if commitment is not None:
            self.commitment = commitment
        if cashaddr is not None:
            self.cashaddr = cashaddr
        if value is not None:
            self.value = value

    @property
    def capability(self):
        """Gets the capability of this TokenMintRequestRequests.  # noqa: E501

        Capability of the new NFT  # noqa: E501

        :return: The capability of this TokenMintRequestRequests.  # noqa: E501
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this TokenMintRequestRequests.

        Capability of the new NFT  # noqa: E501

        :param capability: The capability of this TokenMintRequestRequests.  # noqa: E501
        :type capability: str
        """
        allowed_values = ["none", "mutable", "minting"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and capability not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `capability` ({0}), must be one of {1}"  # noqa: E501
                .format(capability, allowed_values)
            )

        self._capability = capability

    @property
    def commitment(self):
        """Gets the commitment of this TokenMintRequestRequests.  # noqa: E501

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :return: The commitment of this TokenMintRequestRequests.  # noqa: E501
        :rtype: str
        """
        return self._commitment

    @commitment.setter
    def commitment(self, commitment):
        """Sets the commitment of this TokenMintRequestRequests.

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :param commitment: The commitment of this TokenMintRequestRequests.  # noqa: E501
        :type commitment: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commitment is not None and len(commitment) > 80):
            raise ValueError("Invalid value for `commitment`, length must be less than or equal to `80`")  # noqa: E501

        self._commitment = commitment

    @property
    def cashaddr(self):
        """Gets the cashaddr of this TokenMintRequestRequests.  # noqa: E501

        Cashaddress to send tokens to  # noqa: E501

        :return: The cashaddr of this TokenMintRequestRequests.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this TokenMintRequestRequests.

        Cashaddress to send tokens to  # noqa: E501

        :param cashaddr: The cashaddr of this TokenMintRequestRequests.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def value(self):
        """Gets the value of this TokenMintRequestRequests.  # noqa: E501

        Satoshi value to send alongside with tokens  # noqa: E501

        :return: The value of this TokenMintRequestRequests.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TokenMintRequestRequests.

        Satoshi value to send alongside with tokens  # noqa: E501

        :param value: The value of this TokenMintRequestRequests.  # noqa: E501
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
        if not isinstance(other, TokenMintRequestRequests):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenMintRequestRequests):
            return True

        return self.to_dict() != other.to_dict()
