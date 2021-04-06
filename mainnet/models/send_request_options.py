# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.9
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SendRequestOptions(object):
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
        'utxo_ids': 'list[str]',
        'change_address': 'str',
        'slp_aware': 'bool'
    }

    attribute_map = {
        'utxo_ids': 'utxoIds',
        'change_address': 'changeAddress',
        'slp_aware': 'slpAware'
    }

    def __init__(self, utxo_ids=None, change_address=None, slp_aware=None, local_vars_configuration=None):  # noqa: E501
        """SendRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._utxo_ids = None
        self._change_address = None
        self._slp_aware = None
        self.discriminator = None

        if utxo_ids is not None:
            self.utxo_ids = utxo_ids
        if change_address is not None:
            self.change_address = change_address
        if slp_aware is not None:
            self.slp_aware = slp_aware

    @property
    def utxo_ids(self):
        """Gets the utxo_ids of this SendRequestOptions.  # noqa: E501


        :return: The utxo_ids of this SendRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._utxo_ids

    @utxo_ids.setter
    def utxo_ids(self, utxo_ids):
        """Sets the utxo_ids of this SendRequestOptions.


        :param utxo_ids: The utxo_ids of this SendRequestOptions.  # noqa: E501
        :type utxo_ids: list[str]
        """

        self._utxo_ids = utxo_ids

    @property
    def change_address(self):
        """Gets the change_address of this SendRequestOptions.  # noqa: E501

        Cash address to receive change to   # noqa: E501

        :return: The change_address of this SendRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._change_address

    @change_address.setter
    def change_address(self, change_address):
        """Sets the change_address of this SendRequestOptions.

        Cash address to receive change to   # noqa: E501

        :param change_address: The change_address of this SendRequestOptions.  # noqa: E501
        :type change_address: str
        """

        self._change_address = change_address

    @property
    def slp_aware(self):
        """Gets the slp_aware of this SendRequestOptions.  # noqa: E501

        If you have any SLP tokens on the address, you should set `slpAware` to `true` to prevent accidental token burning So far this option is not switched on by default  # noqa: E501

        :return: The slp_aware of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._slp_aware

    @slp_aware.setter
    def slp_aware(self, slp_aware):
        """Sets the slp_aware of this SendRequestOptions.

        If you have any SLP tokens on the address, you should set `slpAware` to `true` to prevent accidental token burning So far this option is not switched on by default  # noqa: E501

        :param slp_aware: The slp_aware of this SendRequestOptions.  # noqa: E501
        :type slp_aware: bool
        """

        self._slp_aware = slp_aware

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
        if not isinstance(other, SendRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
