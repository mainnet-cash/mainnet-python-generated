# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.40
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class MineRequest(object):
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
        'cashaddr': 'str',
        'blocks': 'float'
    }

    attribute_map = {
        'cashaddr': 'cashaddr',
        'blocks': 'blocks'
    }

    def __init__(self, cashaddr=None, blocks=None, local_vars_configuration=None):  # noqa: E501
        """MineRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cashaddr = None
        self._blocks = None
        self.discriminator = None

        if cashaddr is not None:
            self.cashaddr = cashaddr
        if blocks is not None:
            self.blocks = blocks

    @property
    def cashaddr(self):
        """Gets the cashaddr of this MineRequest.  # noqa: E501


        :return: The cashaddr of this MineRequest.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this MineRequest.


        :param cashaddr: The cashaddr of this MineRequest.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def blocks(self):
        """Gets the blocks of this MineRequest.  # noqa: E501

        the number of blocks to mine  # noqa: E501

        :return: The blocks of this MineRequest.  # noqa: E501
        :rtype: float
        """
        return self._blocks

    @blocks.setter
    def blocks(self, blocks):
        """Sets the blocks of this MineRequest.

        the number of blocks to mine  # noqa: E501

        :param blocks: The blocks of this MineRequest.  # noqa: E501
        :type blocks: float
        """

        self._blocks = blocks

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
        if not isinstance(other, MineRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MineRequest):
            return True

        return self.to_dict() != other.to_dict()
