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


class EscrowInfoRequest(object):
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
        'escrow_contract_id': 'str'
    }

    attribute_map = {
        'escrow_contract_id': 'escrowContractId'
    }

    def __init__(self, escrow_contract_id=None, local_vars_configuration=None):  # noqa: E501
        """EscrowInfoRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._escrow_contract_id = None
        self.discriminator = None

        if escrow_contract_id is not None:
            self.escrow_contract_id = escrow_contract_id

    @property
    def escrow_contract_id(self):
        """Gets the escrow_contract_id of this EscrowInfoRequest.  # noqa: E501

        serialized escrow contract   # noqa: E501

        :return: The escrow_contract_id of this EscrowInfoRequest.  # noqa: E501
        :rtype: str
        """
        return self._escrow_contract_id

    @escrow_contract_id.setter
    def escrow_contract_id(self, escrow_contract_id):
        """Sets the escrow_contract_id of this EscrowInfoRequest.

        serialized escrow contract   # noqa: E501

        :param escrow_contract_id: The escrow_contract_id of this EscrowInfoRequest.  # noqa: E501
        :type escrow_contract_id: str
        """

        self._escrow_contract_id = escrow_contract_id

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
        if not isinstance(other, EscrowInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EscrowInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
