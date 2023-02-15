# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.12
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractResponse(object):
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
        'contract_id': 'str',
        'address': 'object'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'address': 'address'
    }

    def __init__(self, contract_id=None, address=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract_id = None
        self._address = None
        self.discriminator = None

        if contract_id is not None:
            self.contract_id = contract_id
        self.address = address

    @property
    def contract_id(self):
        """Gets the contract_id of this SmartBchContractResponse.  # noqa: E501

        serialized contract  # noqa: E501

        :return: The contract_id of this SmartBchContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this SmartBchContractResponse.

        serialized contract  # noqa: E501

        :param contract_id: The contract_id of this SmartBchContractResponse.  # noqa: E501
        :type contract_id: str
        """

        self._contract_id = contract_id

    @property
    def address(self):
        """Gets the address of this SmartBchContractResponse.  # noqa: E501

        Contract address  # noqa: E501

        :return: The address of this SmartBchContractResponse.  # noqa: E501
        :rtype: object
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SmartBchContractResponse.

        Contract address  # noqa: E501

        :param address: The address of this SmartBchContractResponse.  # noqa: E501
        :type address: object
        """

        self._address = address

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
        if not isinstance(other, SmartBchContractResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractResponse):
            return True

        return self.to_dict() != other.to_dict()
