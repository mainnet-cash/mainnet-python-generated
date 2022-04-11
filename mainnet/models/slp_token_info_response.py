# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.39
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SlpTokenInfoResponse(object):
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
        'initial_amount': 'str',
        'decimals': 'float',
        'document_url': 'str',
        'document_hash': 'str',
        'type': 'float'
    }

    attribute_map = {
        'name': 'name',
        'ticker': 'ticker',
        'token_id': 'tokenId',
        'initial_amount': 'initialAmount',
        'decimals': 'decimals',
        'document_url': 'documentUrl',
        'document_hash': 'documentHash',
        'type': 'type'
    }

    def __init__(self, name=None, ticker=None, token_id=None, initial_amount=None, decimals=None, document_url=None, document_hash=None, type=None, local_vars_configuration=None):  # noqa: E501
        """SlpTokenInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._ticker = None
        self._token_id = None
        self._initial_amount = None
        self._decimals = None
        self._document_url = None
        self._document_hash = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ticker is not None:
            self.ticker = ticker
        if token_id is not None:
            self.token_id = token_id
        if initial_amount is not None:
            self.initial_amount = initial_amount
        if decimals is not None:
            self.decimals = decimals
        if document_url is not None:
            self.document_url = document_url
        if document_hash is not None:
            self.document_hash = document_hash
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this SlpTokenInfoResponse.  # noqa: E501

        Token name  # noqa: E501

        :return: The name of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SlpTokenInfoResponse.

        Token name  # noqa: E501

        :param name: The name of this SlpTokenInfoResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this SlpTokenInfoResponse.  # noqa: E501

        Token ticker  # noqa: E501

        :return: The ticker of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this SlpTokenInfoResponse.

        Token ticker  # noqa: E501

        :param ticker: The ticker of this SlpTokenInfoResponse.  # noqa: E501
        :type ticker: str
        """

        self._ticker = ticker

    @property
    def token_id(self):
        """Gets the token_id of this SlpTokenInfoResponse.  # noqa: E501


        :return: The token_id of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SlpTokenInfoResponse.


        :param token_id: The token_id of this SlpTokenInfoResponse.  # noqa: E501
        :type token_id: str
        """

        self._token_id = token_id

    @property
    def initial_amount(self):
        """Gets the initial_amount of this SlpTokenInfoResponse.  # noqa: E501

        Value is represented as a string to avoid precision loss  # noqa: E501

        :return: The initial_amount of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._initial_amount

    @initial_amount.setter
    def initial_amount(self, initial_amount):
        """Sets the initial_amount of this SlpTokenInfoResponse.

        Value is represented as a string to avoid precision loss  # noqa: E501

        :param initial_amount: The initial_amount of this SlpTokenInfoResponse.  # noqa: E501
        :type initial_amount: str
        """

        self._initial_amount = initial_amount

    @property
    def decimals(self):
        """Gets the decimals of this SlpTokenInfoResponse.  # noqa: E501

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :return: The decimals of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SlpTokenInfoResponse.

        Indicates that 1 token is divisible into 10^decimals base units  # noqa: E501

        :param decimals: The decimals of this SlpTokenInfoResponse.  # noqa: E501
        :type decimals: float
        """

        self._decimals = decimals

    @property
    def document_url(self):
        """Gets the document_url of this SlpTokenInfoResponse.  # noqa: E501


        :return: The document_url of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._document_url

    @document_url.setter
    def document_url(self, document_url):
        """Sets the document_url of this SlpTokenInfoResponse.


        :param document_url: The document_url of this SlpTokenInfoResponse.  # noqa: E501
        :type document_url: str
        """

        self._document_url = document_url

    @property
    def document_hash(self):
        """Gets the document_hash of this SlpTokenInfoResponse.  # noqa: E501

        Document hash of the token. Empty or 64 character long hex string.  # noqa: E501

        :return: The document_hash of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._document_hash

    @document_hash.setter
    def document_hash(self, document_hash):
        """Sets the document_hash of this SlpTokenInfoResponse.

        Document hash of the token. Empty or 64 character long hex string.  # noqa: E501

        :param document_hash: The document_hash of this SlpTokenInfoResponse.  # noqa: E501
        :type document_hash: str
        """

        self._document_hash = document_hash

    @property
    def type(self):
        """Gets the type of this SlpTokenInfoResponse.  # noqa: E501

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :return: The type of this SlpTokenInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlpTokenInfoResponse.

        Token type. 0x01 Type1, 0x81 NFT Parent, 0x41 NFT Child  # noqa: E501

        :param type: The type of this SlpTokenInfoResponse.  # noqa: E501
        :type type: float
        """

        self._type = type

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
        if not isinstance(other, SlpTokenInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlpTokenInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
