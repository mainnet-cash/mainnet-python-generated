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


class TokenBurnRequest(object):
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
        'token_id': 'str',
        'capability': 'str',
        'commitment': 'str',
        'amount': 'float',
        'cashaddr': 'str',
        'message': 'str'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'token_id': 'tokenId',
        'capability': 'capability',
        'commitment': 'commitment',
        'amount': 'amount',
        'cashaddr': 'cashaddr',
        'message': 'message'
    }

    def __init__(self, wallet_id=None, token_id=None, capability=None, commitment=None, amount=None, cashaddr=None, message=None, local_vars_configuration=None):  # noqa: E501
        """TokenBurnRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._token_id = None
        self._capability = None
        self._commitment = None
        self._amount = None
        self._cashaddr = None
        self._message = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.token_id = token_id
        if capability is not None:
            self.capability = capability
        if commitment is not None:
            self.commitment = commitment
        if amount is not None:
            self.amount = amount
        if cashaddr is not None:
            self.cashaddr = cashaddr
        if message is not None:
            self.message = message

    @property
    def wallet_id(self):
        """Gets the wallet_id of this TokenBurnRequest.  # noqa: E501

        The walletId to make a request to.  # noqa: E501

        :return: The wallet_id of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this TokenBurnRequest.

        The walletId to make a request to.  # noqa: E501

        :param wallet_id: The wallet_id of this TokenBurnRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def token_id(self):
        """Gets the token_id of this TokenBurnRequest.  # noqa: E501

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :return: The token_id of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this TokenBurnRequest.

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :param token_id: The token_id of this TokenBurnRequest.  # noqa: E501
        :type token_id: str
        """
        if self.local_vars_configuration.client_side_validation and token_id is None:  # noqa: E501
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def capability(self):
        """Gets the capability of this TokenBurnRequest.  # noqa: E501

        Capability of the new NFT  # noqa: E501

        :return: The capability of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this TokenBurnRequest.

        Capability of the new NFT  # noqa: E501

        :param capability: The capability of this TokenBurnRequest.  # noqa: E501
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
        """Gets the commitment of this TokenBurnRequest.  # noqa: E501

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :return: The commitment of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._commitment

    @commitment.setter
    def commitment(self, commitment):
        """Sets the commitment of this TokenBurnRequest.

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :param commitment: The commitment of this TokenBurnRequest.  # noqa: E501
        :type commitment: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commitment is not None and len(commitment) > 80):
            raise ValueError("Invalid value for `commitment`, length must be less than or equal to `80`")  # noqa: E501

        self._commitment = commitment

    @property
    def amount(self):
        """Gets the amount of this TokenBurnRequest.  # noqa: E501

        amount of fungible tokens to burn  # noqa: E501

        :return: The amount of this TokenBurnRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TokenBurnRequest.

        amount of fungible tokens to burn  # noqa: E501

        :param amount: The amount of this TokenBurnRequest.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def cashaddr(self):
        """Gets the cashaddr of this TokenBurnRequest.  # noqa: E501

        address to return token and satoshi change to, default to the sender's cashaddr  # noqa: E501

        :return: The cashaddr of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this TokenBurnRequest.

        address to return token and satoshi change to, default to the sender's cashaddr  # noqa: E501

        :param cashaddr: The cashaddr of this TokenBurnRequest.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def message(self):
        """Gets the message of this TokenBurnRequest.  # noqa: E501

        optional message to include in OP_RETURN  # noqa: E501

        :return: The message of this TokenBurnRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TokenBurnRequest.

        optional message to include in OP_RETURN  # noqa: E501

        :param message: The message of this TokenBurnRequest.  # noqa: E501
        :type message: str
        """

        self._message = message

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
        if not isinstance(other, TokenBurnRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenBurnRequest):
            return True

        return self.to_dict() != other.to_dict()
