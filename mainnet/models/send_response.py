# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.27
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SendResponse(object):
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
        'tx_id': 'str',
        'balance': 'BalanceResponse',
        'explorer_url': 'str',
        'token_ids': 'list[str]'
    }

    attribute_map = {
        'tx_id': 'txId',
        'balance': 'balance',
        'explorer_url': 'explorerUrl',
        'token_ids': 'tokenIds'
    }

    def __init__(self, tx_id=None, balance=None, explorer_url=None, token_ids=None, local_vars_configuration=None):  # noqa: E501
        """SendResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tx_id = None
        self._balance = None
        self._explorer_url = None
        self._token_ids = None
        self.discriminator = None

        if tx_id is not None:
            self.tx_id = tx_id
        if balance is not None:
            self.balance = balance
        if explorer_url is not None:
            self.explorer_url = explorer_url
        if token_ids is not None:
            self.token_ids = token_ids

    @property
    def tx_id(self):
        """Gets the tx_id of this SendResponse.  # noqa: E501

        The hash of a transaction  # noqa: E501

        :return: The tx_id of this SendResponse.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this SendResponse.

        The hash of a transaction  # noqa: E501

        :param tx_id: The tx_id of this SendResponse.  # noqa: E501
        :type tx_id: str
        """

        self._tx_id = tx_id

    @property
    def balance(self):
        """Gets the balance of this SendResponse.  # noqa: E501


        :return: The balance of this SendResponse.  # noqa: E501
        :rtype: BalanceResponse
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SendResponse.


        :param balance: The balance of this SendResponse.  # noqa: E501
        :type balance: BalanceResponse
        """

        self._balance = balance

    @property
    def explorer_url(self):
        """Gets the explorer_url of this SendResponse.  # noqa: E501

        Web url to a transaction on a block explorer  # noqa: E501

        :return: The explorer_url of this SendResponse.  # noqa: E501
        :rtype: str
        """
        return self._explorer_url

    @explorer_url.setter
    def explorer_url(self, explorer_url):
        """Sets the explorer_url of this SendResponse.

        Web url to a transaction on a block explorer  # noqa: E501

        :param explorer_url: The explorer_url of this SendResponse.  # noqa: E501
        :type explorer_url: str
        """

        self._explorer_url = explorer_url

    @property
    def token_ids(self):
        """Gets the token_ids of this SendResponse.  # noqa: E501


        :return: The token_ids of this SendResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._token_ids

    @token_ids.setter
    def token_ids(self, token_ids):
        """Sets the token_ids of this SendResponse.


        :param token_ids: The token_ids of this SendResponse.  # noqa: E501
        :type token_ids: list[str]
        """

        self._token_ids = token_ids

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
        if not isinstance(other, SendResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendResponse):
            return True

        return self.to_dict() != other.to_dict()
