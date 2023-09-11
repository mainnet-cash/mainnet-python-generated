# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.0.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SendRequest(object):
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
        'to': 'AnyOfSendRequestItemarrayTokenSendRequestOpReturnData',
        'options': 'SendRequestOptions'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'to': 'to',
        'options': 'options'
    }

    def __init__(self, wallet_id=None, to=None, options=None, local_vars_configuration=None):  # noqa: E501
        """SendRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._to = None
        self._options = None
        self.discriminator = None

        if wallet_id is not None:
            self.wallet_id = wallet_id
        if to is not None:
            self.to = to
        if options is not None:
            self.options = options

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SendRequest.  # noqa: E501

        The walletId of the source of funds to spend from.   # noqa: E501

        :return: The wallet_id of this SendRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SendRequest.

        The walletId of the source of funds to spend from.   # noqa: E501

        :param wallet_id: The wallet_id of this SendRequest.  # noqa: E501
        :type wallet_id: str
        """

        self._wallet_id = wallet_id

    @property
    def to(self):
        """Gets the to of this SendRequest.  # noqa: E501


        :return: The to of this SendRequest.  # noqa: E501
        :rtype: AnyOfSendRequestItemarrayTokenSendRequestOpReturnData
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendRequest.


        :param to: The to of this SendRequest.  # noqa: E501
        :type to: AnyOfSendRequestItemarrayTokenSendRequestOpReturnData
        """

        self._to = to

    @property
    def options(self):
        """Gets the options of this SendRequest.  # noqa: E501


        :return: The options of this SendRequest.  # noqa: E501
        :rtype: SendRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SendRequest.


        :param options: The options of this SendRequest.  # noqa: E501
        :type options: SendRequestOptions
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
        if not isinstance(other, SendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendRequest):
            return True

        return self.to_dict() != other.to_dict()
