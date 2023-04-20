# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SlpSendMaxRequest(object):
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
        'slpaddr': 'str',
        'token_id': 'str',
        'options': 'SlpSendRequestOptions'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'slpaddr': 'slpaddr',
        'token_id': 'tokenId',
        'options': 'options'
    }

    def __init__(self, wallet_id=None, slpaddr=None, token_id=None, options=None, local_vars_configuration=None):  # noqa: E501
        """SlpSendMaxRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._slpaddr = None
        self._token_id = None
        self._options = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.slpaddr = slpaddr
        self.token_id = token_id
        if options is not None:
            self.options = options

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SlpSendMaxRequest.  # noqa: E501

        The walletId of the sending wallet   # noqa: E501

        :return: The wallet_id of this SlpSendMaxRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SlpSendMaxRequest.

        The walletId of the sending wallet   # noqa: E501

        :param wallet_id: The wallet_id of this SlpSendMaxRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def slpaddr(self):
        """Gets the slpaddr of this SlpSendMaxRequest.  # noqa: E501


        :return: The slpaddr of this SlpSendMaxRequest.  # noqa: E501
        :rtype: str
        """
        return self._slpaddr

    @slpaddr.setter
    def slpaddr(self, slpaddr):
        """Sets the slpaddr of this SlpSendMaxRequest.


        :param slpaddr: The slpaddr of this SlpSendMaxRequest.  # noqa: E501
        :type slpaddr: str
        """
        if self.local_vars_configuration.client_side_validation and slpaddr is None:  # noqa: E501
            raise ValueError("Invalid value for `slpaddr`, must not be `None`")  # noqa: E501

        self._slpaddr = slpaddr

    @property
    def token_id(self):
        """Gets the token_id of this SlpSendMaxRequest.  # noqa: E501

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :return: The token_id of this SlpSendMaxRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this SlpSendMaxRequest.

        Token unique hexadecimal identifier, also the id of the token creation transaction  # noqa: E501

        :param token_id: The token_id of this SlpSendMaxRequest.  # noqa: E501
        :type token_id: str
        """
        if self.local_vars_configuration.client_side_validation and token_id is None:  # noqa: E501
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def options(self):
        """Gets the options of this SlpSendMaxRequest.  # noqa: E501


        :return: The options of this SlpSendMaxRequest.  # noqa: E501
        :rtype: SlpSendRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SlpSendMaxRequest.


        :param options: The options of this SlpSendMaxRequest.  # noqa: E501
        :type options: SlpSendRequestOptions
        """

        self._options = options

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
        if not isinstance(other, SlpSendMaxRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SlpSendMaxRequest):
            return True

        return self.to_dict() != other.to_dict()
