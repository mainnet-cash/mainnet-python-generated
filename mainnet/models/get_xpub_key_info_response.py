# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class GetXpubKeyInfoResponse(object):
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
        'version': 'str',
        'depth': 'float',
        'parent_fingerprint': 'str',
        'data': 'str',
        'chain': 'object'
    }

    attribute_map = {
        'version': 'version',
        'depth': 'depth',
        'parent_fingerprint': 'parentFingerprint',
        'data': 'data',
        'chain': 'chain'
    }

    def __init__(self, version=None, depth=None, parent_fingerprint=None, data=None, chain=None, local_vars_configuration=None):  # noqa: E501
        """GetXpubKeyInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._depth = None
        self._parent_fingerprint = None
        self._data = None
        self._chain = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if depth is not None:
            self.depth = depth
        if parent_fingerprint is not None:
            self.parent_fingerprint = parent_fingerprint
        if data is not None:
            self.data = data
        self.chain = chain

    @property
    def version(self):
        """Gets the version of this GetXpubKeyInfoResponse.  # noqa: E501


        :return: The version of this GetXpubKeyInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetXpubKeyInfoResponse.


        :param version: The version of this GetXpubKeyInfoResponse.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def depth(self):
        """Gets the depth of this GetXpubKeyInfoResponse.  # noqa: E501


        :return: The depth of this GetXpubKeyInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this GetXpubKeyInfoResponse.


        :param depth: The depth of this GetXpubKeyInfoResponse.  # noqa: E501
        :type depth: float
        """

        self._depth = depth

    @property
    def parent_fingerprint(self):
        """Gets the parent_fingerprint of this GetXpubKeyInfoResponse.  # noqa: E501

        the first four bytes of the public key as hex  # noqa: E501

        :return: The parent_fingerprint of this GetXpubKeyInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_fingerprint

    @parent_fingerprint.setter
    def parent_fingerprint(self, parent_fingerprint):
        """Sets the parent_fingerprint of this GetXpubKeyInfoResponse.

        the first four bytes of the public key as hex  # noqa: E501

        :param parent_fingerprint: The parent_fingerprint of this GetXpubKeyInfoResponse.  # noqa: E501
        :type parent_fingerprint: str
        """

        self._parent_fingerprint = parent_fingerprint

    @property
    def data(self):
        """Gets the data of this GetXpubKeyInfoResponse.  # noqa: E501

        the public key as hex  # noqa: E501

        :return: The data of this GetXpubKeyInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetXpubKeyInfoResponse.

        the public key as hex  # noqa: E501

        :param data: The data of this GetXpubKeyInfoResponse.  # noqa: E501
        :type data: str
        """

        self._data = data

    @property
    def chain(self):
        """Gets the chain of this GetXpubKeyInfoResponse.  # noqa: E501

        The chain code, 32 bytes of entrophy extended for the public key  # noqa: E501

        :return: The chain of this GetXpubKeyInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this GetXpubKeyInfoResponse.

        The chain code, 32 bytes of entrophy extended for the public key  # noqa: E501

        :param chain: The chain of this GetXpubKeyInfoResponse.  # noqa: E501
        :type chain: object
        """

        self._chain = chain

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
        if not isinstance(other, GetXpubKeyInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetXpubKeyInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
