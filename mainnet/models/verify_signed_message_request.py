# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.4.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class VerifySignedMessageRequest(object):
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
        'message': 'str',
        'signature': 'object',
        'public_key': 'str'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'message': 'message',
        'signature': 'signature',
        'public_key': 'publicKey'
    }

    def __init__(self, wallet_id=None, message=None, signature=None, public_key=None, local_vars_configuration=None):  # noqa: E501
        """VerifySignedMessageRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._message = None
        self._signature = None
        self._public_key = None
        self.discriminator = None

        if wallet_id is not None:
            self.wallet_id = wallet_id
        if message is not None:
            self.message = message
        self.signature = signature
        if public_key is not None:
            self.public_key = public_key

    @property
    def wallet_id(self):
        """Gets the wallet_id of this VerifySignedMessageRequest.  # noqa: E501


        :return: The wallet_id of this VerifySignedMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this VerifySignedMessageRequest.


        :param wallet_id: The wallet_id of this VerifySignedMessageRequest.  # noqa: E501
        :type wallet_id: str
        """

        self._wallet_id = wallet_id

    @property
    def message(self):
        """Gets the message of this VerifySignedMessageRequest.  # noqa: E501


        :return: The message of this VerifySignedMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this VerifySignedMessageRequest.


        :param message: The message of this VerifySignedMessageRequest.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def signature(self):
        """Gets the signature of this VerifySignedMessageRequest.  # noqa: E501

        The base64 signature of the double sha265 hash of a bitcoin message formatted string signed using the private key associated with the related cashaddr  # noqa: E501

        :return: The signature of this VerifySignedMessageRequest.  # noqa: E501
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this VerifySignedMessageRequest.

        The base64 signature of the double sha265 hash of a bitcoin message formatted string signed using the private key associated with the related cashaddr  # noqa: E501

        :param signature: The signature of this VerifySignedMessageRequest.  # noqa: E501
        :type signature: object
        """

        self._signature = signature

    @property
    def public_key(self):
        """Gets the public_key of this VerifySignedMessageRequest.  # noqa: E501

        If the publicKey is not recoverable from the signature, the base64 encoded public key may be passed as instead of the walletId  # noqa: E501

        :return: The public_key of this VerifySignedMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this VerifySignedMessageRequest.

        If the publicKey is not recoverable from the signature, the base64 encoded public key may be passed as instead of the walletId  # noqa: E501

        :param public_key: The public_key of this VerifySignedMessageRequest.  # noqa: E501
        :type public_key: str
        """

        self._public_key = public_key

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
        if not isinstance(other, VerifySignedMessageRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifySignedMessageRequest):
            return True

        return self.to_dict() != other.to_dict()
