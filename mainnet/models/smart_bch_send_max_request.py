# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchSendMaxRequest(object):
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
        'address': 'str',
        'options': 'SmartBchSendRequestOptions',
        'overrides': 'SmartBchOverrides'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'address': 'address',
        'options': 'options',
        'overrides': 'overrides'
    }

    def __init__(self, wallet_id=None, address=None, options=None, overrides=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchSendMaxRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._address = None
        self._options = None
        self._overrides = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.address = address
        if options is not None:
            self.options = options
        if overrides is not None:
            self.overrides = overrides

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SmartBchSendMaxRequest.  # noqa: E501

        The walletId of the sender   # noqa: E501

        :return: The wallet_id of this SmartBchSendMaxRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SmartBchSendMaxRequest.

        The walletId of the sender   # noqa: E501

        :param wallet_id: The wallet_id of this SmartBchSendMaxRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def address(self):
        """Gets the address of this SmartBchSendMaxRequest.  # noqa: E501


        :return: The address of this SmartBchSendMaxRequest.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SmartBchSendMaxRequest.


        :param address: The address of this SmartBchSendMaxRequest.  # noqa: E501
        :type address: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def options(self):
        """Gets the options of this SmartBchSendMaxRequest.  # noqa: E501


        :return: The options of this SmartBchSendMaxRequest.  # noqa: E501
        :rtype: SmartBchSendRequestOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SmartBchSendMaxRequest.


        :param options: The options of this SmartBchSendMaxRequest.  # noqa: E501
        :type options: SmartBchSendRequestOptions
        """

        self._options = options

    @property
    def overrides(self):
        """Gets the overrides of this SmartBchSendMaxRequest.  # noqa: E501


        :return: The overrides of this SmartBchSendMaxRequest.  # noqa: E501
        :rtype: SmartBchOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this SmartBchSendMaxRequest.


        :param overrides: The overrides of this SmartBchSendMaxRequest.  # noqa: E501
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
        if not isinstance(other, SmartBchSendMaxRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchSendMaxRequest):
            return True

        return self.to_dict() != other.to_dict()
