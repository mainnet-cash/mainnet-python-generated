# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.19
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class VerifySignedMessageResponseDetails(object):
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
        'signature_type': 'str',
        'message_hash': 'str',
        'signature_valid': 'bool',
        'public_key_hash_match': 'bool'
    }

    attribute_map = {
        'signature_type': 'signatureType',
        'message_hash': 'messageHash',
        'signature_valid': 'signatureValid',
        'public_key_hash_match': 'publicKeyHashMatch'
    }

    def __init__(self, signature_type=None, message_hash=None, signature_valid=None, public_key_hash_match=None, local_vars_configuration=None):  # noqa: E501
        """VerifySignedMessageResponseDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signature_type = None
        self._message_hash = None
        self._signature_valid = None
        self._public_key_hash_match = None
        self.discriminator = None

        if signature_type is not None:
            self.signature_type = signature_type
        if message_hash is not None:
            self.message_hash = message_hash
        if signature_valid is not None:
            self.signature_valid = signature_valid
        if public_key_hash_match is not None:
            self.public_key_hash_match = public_key_hash_match

    @property
    def signature_type(self):
        """Gets the signature_type of this VerifySignedMessageResponseDetails.  # noqa: E501

        The type of signature passed  # noqa: E501

        :return: The signature_type of this VerifySignedMessageResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this VerifySignedMessageResponseDetails.

        The type of signature passed  # noqa: E501

        :param signature_type: The signature_type of this VerifySignedMessageResponseDetails.  # noqa: E501
        :type signature_type: str
        """

        self._signature_type = signature_type

    @property
    def message_hash(self):
        """Gets the message_hash of this VerifySignedMessageResponseDetails.  # noqa: E501

        The double sha256 hash of the string encoded as Bitcoin Message binary.  # noqa: E501

        :return: The message_hash of this VerifySignedMessageResponseDetails.  # noqa: E501
        :rtype: str
        """
        return self._message_hash

    @message_hash.setter
    def message_hash(self, message_hash):
        """Sets the message_hash of this VerifySignedMessageResponseDetails.

        The double sha256 hash of the string encoded as Bitcoin Message binary.  # noqa: E501

        :param message_hash: The message_hash of this VerifySignedMessageResponseDetails.  # noqa: E501
        :type message_hash: str
        """

        self._message_hash = message_hash

    @property
    def signature_valid(self):
        """Gets the signature_valid of this VerifySignedMessageResponseDetails.  # noqa: E501

        A boolean indicating whether the signature is valid for the message  # noqa: E501

        :return: The signature_valid of this VerifySignedMessageResponseDetails.  # noqa: E501
        :rtype: bool
        """
        return self._signature_valid

    @signature_valid.setter
    def signature_valid(self, signature_valid):
        """Sets the signature_valid of this VerifySignedMessageResponseDetails.

        A boolean indicating whether the signature is valid for the message  # noqa: E501

        :param signature_valid: The signature_valid of this VerifySignedMessageResponseDetails.  # noqa: E501
        :type signature_valid: bool
        """

        self._signature_valid = signature_valid

    @property
    def public_key_hash_match(self):
        """Gets the public_key_hash_match of this VerifySignedMessageResponseDetails.  # noqa: E501

        A boolean indicating whether the publicKeyHash of a recoverable signature matches the provided cashaddr, false otherwise  # noqa: E501

        :return: The public_key_hash_match of this VerifySignedMessageResponseDetails.  # noqa: E501
        :rtype: bool
        """
        return self._public_key_hash_match

    @public_key_hash_match.setter
    def public_key_hash_match(self, public_key_hash_match):
        """Sets the public_key_hash_match of this VerifySignedMessageResponseDetails.

        A boolean indicating whether the publicKeyHash of a recoverable signature matches the provided cashaddr, false otherwise  # noqa: E501

        :param public_key_hash_match: The public_key_hash_match of this VerifySignedMessageResponseDetails.  # noqa: E501
        :type public_key_hash_match: bool
        """

        self._public_key_hash_match = public_key_hash_match

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
        if not isinstance(other, VerifySignedMessageResponseDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifySignedMessageResponseDetails):
            return True

        return self.to_dict() != other.to_dict()
