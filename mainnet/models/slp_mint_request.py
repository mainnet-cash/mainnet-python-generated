# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.14
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SlpMintRequest(object):
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
        'value': 'str',
        'token_id': 'str',
        'end_baton': 'bool',
        'token_receiver_slp_addr': 'str',
        'baton_receiver_slp_addr': 'str'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'value': 'value',
        'token_id': 'tokenId',
        'end_baton': 'endBaton',
        'token_receiver_slp_addr': 'tokenReceiverSlpAddr',
        'baton_receiver_slp_addr': 'batonReceiverSlpAddr'
    }

    def __init__(self, wallet_id=None, value=None, token_id=None, end_baton=None, token_receiver_slp_addr=None, baton_receiver_slp_addr=None, local_vars_configuration=None):  # noqa: E501
        """SlpMintRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._value = None
        self._token_id = None
        self._end_baton = None
        self._token_receiver_slp_addr = None
        self._baton_receiver_slp_addr = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.value = value
        self.token_id = token_id
        if end_baton is not None:
            self.end_baton = end_baton
        if token_receiver_slp_addr is not None:
            self.token_receiver_slp_addr = token_receiver_slp_addr
        if baton_receiver_slp_addr is not None:
            self.baton_receiver_slp_addr = baton_receiver_slp_addr

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SlpMintRequest.  # noqa: E501

        ID that is returned in `wallet` field of /wallet call   # noqa: E501

        :return: The wallet_id of this SlpMintRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SlpMintRequest.

        ID that is returned in `wallet` field of /wallet call   # noqa: E501

        :param wallet_id: The wallet_id of this SlpMintRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def value(self):
        """Gets the value of this SlpMintRequest.  # noqa: E501

        Value is represented as a string to avoid precision loss  # noqa: E501

        :return: The value of this SlpMintRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SlpMintRequest.

        Value is represented as a string to avoid precision loss  # noqa: E501

        :param value: The value of this SlpMintRequest.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def token_id(self):
        """Gets the token_id of this SlpMintRequest.  # noqa: E501


        :return: The token_id of this SlpMintRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SlpMintRequest.


        :param token_id: The token_id of this SlpMintRequest.  # noqa: E501
        :type token_id: str
        """
        if self.local_vars_configuration.client_side_validation and token_id is None:  # noqa: E501
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def end_baton(self):
        """Gets the end_baton of this SlpMintRequest.  # noqa: E501

        Indicates if token should not be 'mintable' anymore, e.g. total circulation amount increased  # noqa: E501

        :return: The end_baton of this SlpMintRequest.  # noqa: E501
        :rtype: bool
        """
        return self._end_baton

    @end_baton.setter
    def end_baton(self, end_baton):
        """Sets the end_baton of this SlpMintRequest.

        Indicates if token should not be 'mintable' anymore, e.g. total circulation amount increased  # noqa: E501

        :param end_baton: The end_baton of this SlpMintRequest.  # noqa: E501
        :type end_baton: bool
        """

        self._end_baton = end_baton

    @property
    def token_receiver_slp_addr(self):
        """Gets the token_receiver_slp_addr of this SlpMintRequest.  # noqa: E501


        :return: The token_receiver_slp_addr of this SlpMintRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_receiver_slp_addr

    @token_receiver_slp_addr.setter
    def token_receiver_slp_addr(self, token_receiver_slp_addr):
        """Sets the token_receiver_slp_addr of this SlpMintRequest.


        :param token_receiver_slp_addr: The token_receiver_slp_addr of this SlpMintRequest.  # noqa: E501
        :type token_receiver_slp_addr: str
        """

        self._token_receiver_slp_addr = token_receiver_slp_addr

    @property
    def baton_receiver_slp_addr(self):
        """Gets the baton_receiver_slp_addr of this SlpMintRequest.  # noqa: E501


        :return: The baton_receiver_slp_addr of this SlpMintRequest.  # noqa: E501
        :rtype: str
        """
        return self._baton_receiver_slp_addr

    @baton_receiver_slp_addr.setter
    def baton_receiver_slp_addr(self, baton_receiver_slp_addr):
        """Sets the baton_receiver_slp_addr of this SlpMintRequest.


        :param baton_receiver_slp_addr: The baton_receiver_slp_addr of this SlpMintRequest.  # noqa: E501
        :type baton_receiver_slp_addr: str
        """

        self._baton_receiver_slp_addr = baton_receiver_slp_addr

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
        if not isinstance(other, SlpMintRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlpMintRequest):
            return True

        return self.to_dict() != other.to_dict()
