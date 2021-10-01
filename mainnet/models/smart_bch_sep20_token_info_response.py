# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.20
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchSep20TokenInfoResponse(object):
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
        'ticker': 'str',
        'token_id': 'str',
        'decimals': 'float',
        'total_supply': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ticker': 'ticker',
        'token_id': 'tokenId',
        'decimals': 'decimals',
        'total_supply': 'totalSupply'
    }

    def __init__(self, name=None, ticker=None, token_id=None, decimals=None, total_supply=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchSep20TokenInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._ticker = None
        self._token_id = None
        self._decimals = None
        self._total_supply = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ticker is not None:
            self.ticker = ticker
        if token_id is not None:
            self.token_id = token_id
        if decimals is not None:
            self.decimals = decimals
        if total_supply is not None:
            self.total_supply = total_supply

    @property
    def name(self):
        """Gets the name of this SmartBchSep20TokenInfoResponse.  # noqa: E501

        Token name  # noqa: E501

        :return: The name of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmartBchSep20TokenInfoResponse.

        Token name  # noqa: E501

        :param name: The name of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this SmartBchSep20TokenInfoResponse.  # noqa: E501

        Token ticker  # noqa: E501

        :return: The ticker of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SmartBchSep20TokenInfoResponse.

        Token ticker  # noqa: E501

        :param ticker: The ticker of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :type ticker: str
        """

        self._ticker = ticker

    @property
    def token_id(self):
        """Gets the token_id of this SmartBchSep20TokenInfoResponse.  # noqa: E501


        :return: The token_id of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SmartBchSep20TokenInfoResponse.


        :param token_id: The token_id of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def decimals(self):
        """Gets the decimals of this SmartBchSep20TokenInfoResponse.  # noqa: E501

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :return: The decimals of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SmartBchSep20TokenInfoResponse.

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :param decimals: The decimals of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :type decimals: float
        """

        self._decimals = decimals

    @property
    def total_supply(self):
        """Gets the total_supply of this SmartBchSep20TokenInfoResponse.  # noqa: E501

        Total amount of tokens in circulation  # noqa: E501

        :return: The total_supply of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_supply

    @total_supply.setter
    def total_supply(self, total_supply):
        """Sets the total_supply of this SmartBchSep20TokenInfoResponse.

        Total amount of tokens in circulation  # noqa: E501

        :param total_supply: The total_supply of this SmartBchSep20TokenInfoResponse.  # noqa: E501
        :type total_supply: str
        """

        self._total_supply = total_supply

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
        if not isinstance(other, SmartBchSep20TokenInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchSep20TokenInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
