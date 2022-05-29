# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.5.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchSep20GenesisRequest(object):
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
        'ticker': 'str',
        'initial_amount': 'AnyOfnumberstring',
        'decimals': 'float',
        'end_baton': 'bool',
        'token_receiver_address': 'str',
        'baton_receiver_address': 'str',
        'overrides': 'SmartBchOverrides'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'name': 'name',
        'ticker': 'ticker',
        'initial_amount': 'initialAmount',
        'decimals': 'decimals',
        'end_baton': 'endBaton',
        'token_receiver_address': 'tokenReceiverAddress',
        'baton_receiver_address': 'batonReceiverAddress',
        'overrides': 'overrides'
    }

    def __init__(self, wallet_id=None, name=None, ticker=None, initial_amount=None, decimals=None, end_baton=None, token_receiver_address=None, baton_receiver_address=None, overrides=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchSep20GenesisRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._name = None
        self._ticker = None
        self._initial_amount = None
        self._decimals = None
        self._end_baton = None
        self._token_receiver_address = None
        self._baton_receiver_address = None
        self._overrides = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.name = name
        self.ticker = ticker
        self.initial_amount = initial_amount
        self.decimals = decimals
        if end_baton is not None:
            self.end_baton = end_baton
        if token_receiver_address is not None:
            self.token_receiver_address = token_receiver_address
        if baton_receiver_address is not None:
            self.baton_receiver_address = baton_receiver_address
        if overrides is not None:
            self.overrides = overrides

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SmartBchSep20GenesisRequest.  # noqa: E501

        serialized wallet  # noqa: E501

        :return: The wallet_id of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SmartBchSep20GenesisRequest.

        serialized wallet  # noqa: E501

        :param wallet_id: The wallet_id of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def name(self):
        """Gets the name of this SmartBchSep20GenesisRequest.  # noqa: E501

        Token name  # noqa: E501

        :return: The name of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SmartBchSep20GenesisRequest.

        Token name  # noqa: E501

        :param name: The name of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this SmartBchSep20GenesisRequest.  # noqa: E501

        Token ticker  # noqa: E501

        :return: The ticker of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SmartBchSep20GenesisRequest.

        Token ticker  # noqa: E501

        :param ticker: The ticker of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type ticker: str
        """
        if self.local_vars_configuration.client_side_validation and ticker is None:  # noqa: E501
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def initial_amount(self):
        """Gets the initial_amount of this SmartBchSep20GenesisRequest.  # noqa: E501

        Value is represented as number or string to avoid precision loss  # noqa: E501

        :return: The initial_amount of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._initial_amount

    @initial_amount.setter
    def initial_amount(self, initial_amount):
        """Sets the initial_amount of this SmartBchSep20GenesisRequest.

        Value is represented as number or string to avoid precision loss  # noqa: E501

        :param initial_amount: The initial_amount of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type initial_amount: AnyOfnumberstring
        """
        if self.local_vars_configuration.client_side_validation and initial_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_amount`, must not be `None`")  # noqa: E501

        self._initial_amount = initial_amount

    @property
    def decimals(self):
        """Gets the decimals of this SmartBchSep20GenesisRequest.  # noqa: E501

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :return: The decimals of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SmartBchSep20GenesisRequest.

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :param decimals: The decimals of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type decimals: float
        """
        if self.local_vars_configuration.client_side_validation and decimals is None:  # noqa: E501
            raise ValueError("Invalid value for `decimals`, must not be `None`")  # noqa: E501

        self._decimals = decimals

    @property
    def end_baton(self):
        """Gets the end_baton of this SmartBchSep20GenesisRequest.  # noqa: E501

        Indicates if token should not be 'mintable', e.g. total circulation amount increased  # noqa: E501

        :return: The end_baton of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._end_baton

    @end_baton.setter
    def end_baton(self, end_baton):
        """Sets the end_baton of this SmartBchSep20GenesisRequest.

        Indicates if token should not be 'mintable', e.g. total circulation amount increased  # noqa: E501

        :param end_baton: The end_baton of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type end_baton: bool
        """

        self._end_baton = end_baton

    @property
    def token_receiver_address(self):
        """Gets the token_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501


        :return: The token_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_receiver_address

    @token_receiver_address.setter
    def token_receiver_address(self, token_receiver_address):
        """Sets the token_receiver_address of this SmartBchSep20GenesisRequest.


        :param token_receiver_address: The token_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type token_receiver_address: str
        """

        self._token_receiver_address = token_receiver_address

    @property
    def baton_receiver_address(self):
        """Gets the baton_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501


        :return: The baton_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: str
        """
        return self._baton_receiver_address

    @baton_receiver_address.setter
    def baton_receiver_address(self, baton_receiver_address):
        """Sets the baton_receiver_address of this SmartBchSep20GenesisRequest.


        :param baton_receiver_address: The baton_receiver_address of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type baton_receiver_address: str
        """

        self._baton_receiver_address = baton_receiver_address

    @property
    def overrides(self):
        """Gets the overrides of this SmartBchSep20GenesisRequest.  # noqa: E501


        :return: The overrides of this SmartBchSep20GenesisRequest.  # noqa: E501
        :rtype: SmartBchOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this SmartBchSep20GenesisRequest.


        :param overrides: The overrides of this SmartBchSep20GenesisRequest.  # noqa: E501
        :type overrides: SmartBchOverrides
        """

        self._overrides = overrides

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
        if not isinstance(other, SmartBchSep20GenesisRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchSep20GenesisRequest):
            return True

        return self.to_dict() != other.to_dict()
