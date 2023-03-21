# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.18
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class TokenGenesisRequest(object):
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
        'amount': 'float',
        'capability': 'str',
        'commitment': 'str',
        'cashaddr': 'str',
        'value': 'float',
        'send_requests': 'AnyOfSendRequestItemarrayTokenSendRequestOpReturnData'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'amount': 'amount',
        'capability': 'capability',
        'commitment': 'commitment',
        'cashaddr': 'cashaddr',
        'value': 'value',
        'send_requests': 'sendRequests'
    }

    def __init__(self, wallet_id=None, amount=None, capability=None, commitment=None, cashaddr=None, value=1000, send_requests=None, local_vars_configuration=None):  # noqa: E501
        """TokenGenesisRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._amount = None
        self._capability = None
        self._commitment = None
        self._cashaddr = None
        self._value = None
        self._send_requests = None
        self.discriminator = None

        self.wallet_id = wallet_id
        if amount is not None:
            self.amount = amount
        if capability is not None:
            self.capability = capability
        if commitment is not None:
            self.commitment = commitment
        if cashaddr is not None:
            self.cashaddr = cashaddr
        if value is not None:
            self.value = value
        if send_requests is not None:
            self.send_requests = send_requests

    @property
    def wallet_id(self):
        """Gets the wallet_id of this TokenGenesisRequest.  # noqa: E501

        The walletId to make a request to.  # noqa: E501

        :return: The wallet_id of this TokenGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this TokenGenesisRequest.

        The walletId to make a request to.  # noqa: E501

        :param wallet_id: The wallet_id of this TokenGenesisRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def amount(self):
        """Gets the amount of this TokenGenesisRequest.  # noqa: E501

        amount of *fungible* tokens to create  # noqa: E501

        :return: The amount of this TokenGenesisRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TokenGenesisRequest.

        amount of *fungible* tokens to create  # noqa: E501

        :param amount: The amount of this TokenGenesisRequest.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def capability(self):
        """Gets the capability of this TokenGenesisRequest.  # noqa: E501

        Capability of the new NFT  # noqa: E501

        :return: The capability of this TokenGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._capability

    @capability.setter
    def capability(self, capability):
        """Sets the capability of this TokenGenesisRequest.

        Capability of the new NFT  # noqa: E501

        :param capability: The capability of this TokenGenesisRequest.  # noqa: E501
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
        """Gets the commitment of this TokenGenesisRequest.  # noqa: E501

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :return: The commitment of this TokenGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._commitment

    @commitment.setter
    def commitment(self, commitment):
        """Sets the commitment of this TokenGenesisRequest.

        Token commitment message, hexadecimal encoded, 40 bytes max length  # noqa: E501

        :param commitment: The commitment of this TokenGenesisRequest.  # noqa: E501
        :type commitment: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commitment is not None and len(commitment) > 80):
            raise ValueError("Invalid value for `commitment`, length must be less than or equal to `80`")  # noqa: E501

        self._commitment = commitment

    @property
    def cashaddr(self):
        """Gets the cashaddr of this TokenGenesisRequest.  # noqa: E501

        Cashaddress to send tokens to  # noqa: E501

        :return: The cashaddr of this TokenGenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this TokenGenesisRequest.

        Cashaddress to send tokens to  # noqa: E501

        :param cashaddr: The cashaddr of this TokenGenesisRequest.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def value(self):
        """Gets the value of this TokenGenesisRequest.  # noqa: E501

        Satoshi value to send alongside with tokens  # noqa: E501

        :return: The value of this TokenGenesisRequest.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TokenGenesisRequest.

        Satoshi value to send alongside with tokens  # noqa: E501

        :param value: The value of this TokenGenesisRequest.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def send_requests(self):
        """Gets the send_requests of this TokenGenesisRequest.  # noqa: E501

        Single or an array of extra send requests (OP_RETURN, value transfer, etc.) to include in genesis transaction.  # noqa: E501

        :return: The send_requests of this TokenGenesisRequest.  # noqa: E501
        :rtype: AnyOfSendRequestItemarrayTokenSendRequestOpReturnData
        """
        return self._send_requests

    @send_requests.setter
    def send_requests(self, send_requests):
        """Sets the send_requests of this TokenGenesisRequest.

        Single or an array of extra send requests (OP_RETURN, value transfer, etc.) to include in genesis transaction.  # noqa: E501

        :param send_requests: The send_requests of this TokenGenesisRequest.  # noqa: E501
        :type send_requests: AnyOfSendRequestItemarrayTokenSendRequestOpReturnData
        """

        self._send_requests = send_requests

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
        if not isinstance(other, TokenGenesisRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenGenesisRequest):
            return True

        return self.to_dict() != other.to_dict()
