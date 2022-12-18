# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractEstimateGasResponse(object):
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
        'gas': 'AnyOfnumberstring'
    }

    attribute_map = {
        'gas': 'gas'
    }

    def __init__(self, gas=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractEstimateGasResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gas = None
        self.discriminator = None

        if gas is not None:
            self.gas = gas

    @property
    def gas(self):
        """Gets the gas of this SmartBchContractEstimateGasResponse.  # noqa: E501


        :return: The gas of this SmartBchContractEstimateGasResponse.  # noqa: E501
        :rtype: AnyOfnumberstring
        """
        return self._gas

    @gas.setter
    def gas(self, gas):
        """Sets the gas of this SmartBchContractEstimateGasResponse.


        :param gas: The gas of this SmartBchContractEstimateGasResponse.  # noqa: E501
        :type gas: AnyOfnumberstring
        """

        self._gas = gas

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
        if not isinstance(other, SmartBchContractEstimateGasResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractEstimateGasResponse):
            return True

        return self.to_dict() != other.to_dict()
