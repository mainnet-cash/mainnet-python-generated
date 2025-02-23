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


class TokenAmountChange(object):
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
        'token_id': 'str',
        'amount': 'float',
        'nft_amount': 'float'
    }

    attribute_map = {
        'token_id': 'tokenId',
        'amount': 'amount',
        'nft_amount': 'nftAmount'
    }

    def __init__(self, token_id=None, amount=None, nft_amount=None, local_vars_configuration=None):  # noqa: E501
        """TokenAmountChange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token_id = None
        self._amount = None
        self._nft_amount = None
        self.discriminator = None

        if token_id is not None:
            self.token_id = token_id
        if amount is not None:
            self.amount = amount
        if nft_amount is not None:
            self.nft_amount = nft_amount

    @property
    def token_id(self):
        """Gets the token_id of this TokenAmountChange.  # noqa: E501

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :return: The token_id of this TokenAmountChange.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this TokenAmountChange.

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :param token_id: The token_id of this TokenAmountChange.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def amount(self):
        """Gets the amount of this TokenAmountChange.  # noqa: E501

        Fungible token amount  # noqa: E501

        :return: The amount of this TokenAmountChange.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TokenAmountChange.

        Fungible token amount  # noqa: E501

        :param amount: The amount of this TokenAmountChange.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def nft_amount(self):
        """Gets the nft_amount of this TokenAmountChange.  # noqa: E501

        Non-fungible token amount  # noqa: E501

        :return: The nft_amount of this TokenAmountChange.  # noqa: E501
        :rtype: float
        """
        return self._nft_amount

    @nft_amount.setter
    def nft_amount(self, nft_amount):
        """Sets the nft_amount of this TokenAmountChange.

        Non-fungible token amount  # noqa: E501

        :param nft_amount: The nft_amount of this TokenAmountChange.  # noqa: E501
        :type nft_amount: float
        """

        self._nft_amount = nft_amount

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
        if not isinstance(other, TokenAmountChange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenAmountChange):
            return True

        return self.to_dict() != other.to_dict()
