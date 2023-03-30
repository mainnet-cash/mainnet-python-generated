# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class UtxoToken(object):
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
        'amount': 'float',
        'token_id': 'str',
        'capability': 'str',
        'commitment': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'token_id': 'tokenId',
        'capability': 'capability',
        'commitment': 'commitment'
    }

    def __init__(self, amount=None, token_id=None, capability=None, commitment=None, local_vars_configuration=None):  # noqa: E501
        """UtxoToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._token_id = None
        self._capability = None
        self._commitment = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if token_id is not None:
            self.token_id = token_id
        self.capability = capability
        self.commitment = commitment

    @property
    def amount(self):
        """Gets the amount of this UtxoToken.  # noqa: E501

        Fungible token amount to send  # noqa: E501

        :return: The amount of this UtxoToken.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UtxoToken.

        Fungible token amount to send  # noqa: E501

        :param amount: The amount of this UtxoToken.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def token_id(self):
        """Gets the token_id of this UtxoToken.  # noqa: E501

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :return: The token_id of this UtxoToken.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this UtxoToken.

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :param token_id: The token_id of this UtxoToken.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def capability(self):
        """Gets the capability of this UtxoToken.  # noqa: E501

        Capability of the NFT  # noqa: E501

        :return: The capability of this UtxoToken.  # noqa: E501
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this UtxoToken.

        Capability of the NFT  # noqa: E501

        :param capability: The capability of this UtxoToken.  # noqa: E501
        :type capability: str
        """
        allowed_values = [None,"none", "mutable", "minting"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and capability not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `capability` ({0}), must be one of {1}"  # noqa: E501
                .format(capability, allowed_values)
            )

        self._capability = capability

    @property
    def commitment(self):
        """Gets the commitment of this UtxoToken.  # noqa: E501

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :return: The commitment of this UtxoToken.  # noqa: E501
        :rtype: str
        """
        return self._commitment

    @commitment.setter
    def commitment(self, commitment):
        """Sets the commitment of this UtxoToken.

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :param commitment: The commitment of this UtxoToken.  # noqa: E501
        :type commitment: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commitment is not None and len(commitment) > 80):
            raise ValueError("Invalid value for `commitment`, length must be less than or equal to `80`")  # noqa: E501

        self._commitment = commitment

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
        if not isinstance(other, UtxoToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UtxoToken):
            return True

        return self.to_dict() != other.to_dict()
