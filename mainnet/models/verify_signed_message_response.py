# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.25
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class VerifySignedMessageResponse(object):
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
        'valid': 'bool',
        'details': 'VerifySignedMessageResponseDetails'
    }

    attribute_map = {
        'valid': 'valid',
        'details': 'details'
    }

    def __init__(self, valid=None, details=None, local_vars_configuration=None):  # noqa: E501
        """VerifySignedMessageResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._valid = None
        self._details = None
        self.discriminator = None

        if valid is not None:
            self.valid = valid
        if details is not None:
            self.details = details

    @property
    def valid(self):
        """Gets the valid of this VerifySignedMessageResponse.  # noqa: E501

        Whether the message was signed by a given address  # noqa: E501

        :return: The valid of this VerifySignedMessageResponse.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this VerifySignedMessageResponse.

        Whether the message was signed by a given address  # noqa: E501

        :param valid: The valid of this VerifySignedMessageResponse.  # noqa: E501
        :type valid: bool
        """

        self._valid = valid

    @property
    def details(self):
        """Gets the details of this VerifySignedMessageResponse.  # noqa: E501


        :return: The details of this VerifySignedMessageResponse.  # noqa: E501
        :rtype: VerifySignedMessageResponseDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this VerifySignedMessageResponse.


        :param details: The details of this VerifySignedMessageResponse.  # noqa: E501
        :type details: VerifySignedMessageResponseDetails
        """

        self._details = details

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
        if not isinstance(other, VerifySignedMessageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifySignedMessageResponse):
            return True

        return self.to_dict() != other.to_dict()
