# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.15
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SignedMessageResponse(object):
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
        'signature': 'str',
        'raw': 'SignedMessageResponseRaw',
        'details': 'SignedMessageResponseDetails'
    }

    attribute_map = {
        'signature': 'signature',
        'raw': 'raw',
        'details': 'details'
    }

    def __init__(self, signature=None, raw=None, details=None, local_vars_configuration=None):  # noqa: E501
        """SignedMessageResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signature = None
        self._raw = None
        self._details = None
        self.discriminator = None

        if signature is not None:
            self.signature = signature
        if raw is not None:
            self.raw = raw
        if details is not None:
            self.details = details

    @property
    def signature(self):
        """Gets the signature of this SignedMessageResponse.  # noqa: E501


        :return: The signature of this SignedMessageResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this SignedMessageResponse.


        :param signature: The signature of this SignedMessageResponse.  # noqa: E501
        :type signature: str
        """

        self._signature = signature

    @property
    def raw(self):
        """Gets the raw of this SignedMessageResponse.  # noqa: E501


        :return: The raw of this SignedMessageResponse.  # noqa: E501
        :rtype: SignedMessageResponseRaw
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this SignedMessageResponse.


        :param raw: The raw of this SignedMessageResponse.  # noqa: E501
        :type raw: SignedMessageResponseRaw
        """

        self._raw = raw

    @property
    def details(self):
        """Gets the details of this SignedMessageResponse.  # noqa: E501


        :return: The details of this SignedMessageResponse.  # noqa: E501
        :rtype: SignedMessageResponseDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SignedMessageResponse.


        :param details: The details of this SignedMessageResponse.  # noqa: E501
        :type details: SignedMessageResponseDetails
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
        if not isinstance(other, SignedMessageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignedMessageResponse):
            return True

        return self.to_dict() != other.to_dict()
