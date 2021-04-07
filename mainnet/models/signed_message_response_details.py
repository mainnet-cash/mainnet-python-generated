# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.12
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SignedMessageResponseDetails(object):
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
        'recovery_id': 'float',
        'compressed': 'bool',
        'message_hash': 'str'
    }

    attribute_map = {
        'recovery_id': 'recoveryId',
        'compressed': 'compressed',
        'message_hash': 'messageHash'
    }

    def __init__(self, recovery_id=None, compressed=None, message_hash=None, local_vars_configuration=None):  # noqa: E501
        """SignedMessageResponseDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recovery_id = None
        self._compressed = None
        self._message_hash = None
        self.discriminator = None

        if recovery_id is not None:
            self.recovery_id = recovery_id
        if compressed is not None:
            self.compressed = compressed
        if message_hash is not None:
            self.message_hash = message_hash

    @property
    def recovery_id(self):
        """Gets the recovery_id of this SignedMessageResponseDetails.  # noqa: E501

        A tag used for recovering the public key from a compact signature.  # noqa: E501

        :return: The recovery_id of this SignedMessageResponseDetails.  # noqa: E501
        :rtype: float
        """
        return self._recovery_id

    @recovery_id.setter
    def recovery_id(self, recovery_id):
        """Sets the recovery_id of this SignedMessageResponseDetails.

        A tag used for recovering the public key from a compact signature.  # noqa: E501

        :param recovery_id: The recovery_id of this SignedMessageResponseDetails.  # noqa: E501
        :type recovery_id: float
        """

        self._recovery_id = recovery_id

    @property
    def compressed(self):
        """Gets the compressed of this SignedMessageResponseDetails.  # noqa: E501


        :return: The compressed of this SignedMessageResponseDetails.  # noqa: E501
        :rtype: bool
        """
        return self._compressed

    @compressed.setter
    def compressed(self, compressed):
        """Sets the compressed of this SignedMessageResponseDetails.


        :param compressed: The compressed of this SignedMessageResponseDetails.  # noqa: E501
        :type compressed: bool
        """

        self._compressed = compressed

    @property
    def message_hash(self):
        """Gets the message_hash of this SignedMessageResponseDetails.  # noqa: E501

        The double sha256 hash of the string encoded as Bitcoin Message binary.  # noqa: E501

        :return: The message_hash of this SignedMessageResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._message_hash

    @message_hash.setter
    def message_hash(self, message_hash):
        """Sets the message_hash of this SignedMessageResponseDetails.

        The double sha256 hash of the string encoded as Bitcoin Message binary.  # noqa: E501

        :param message_hash: The message_hash of this SignedMessageResponseDetails.  # noqa: E501
        :type message_hash: str
        """

        self._message_hash = message_hash

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
        if not isinstance(other, SignedMessageResponseDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SignedMessageResponseDetails):
            return True

        return self.to_dict() != other.to_dict()
