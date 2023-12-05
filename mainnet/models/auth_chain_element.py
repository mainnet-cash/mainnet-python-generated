# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class AuthChainElement(object):
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
        'tx_hash': 'str',
        'content_hash': 'str',
        'uris': 'list[str]',
        'https_url': 'str'
    }

    attribute_map = {
        'tx_hash': 'txHash',
        'content_hash': 'contentHash',
        'uris': 'uris',
        'https_url': 'httpsUrl'
    }

    def __init__(self, tx_hash=None, content_hash=None, uris=None, https_url=None, local_vars_configuration=None):  # noqa: E501
        """AuthChainElement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tx_hash = None
        self._content_hash = None
        self._uris = None
        self._https_url = None
        self.discriminator = None

        if tx_hash is not None:
            self.tx_hash = tx_hash
        if content_hash is not None:
            self.content_hash = content_hash
        if uris is not None:
            self.uris = uris
        if https_url is not None:
            self.https_url = https_url

    @property
    def tx_hash(self):
        """Gets the tx_hash of this AuthChainElement.  # noqa: E501

        Hex encoded transaction hash  # noqa: E501

        :return: The tx_hash of this AuthChainElement.  # noqa: E501
        :rtype: str
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this AuthChainElement.

        Hex encoded transaction hash  # noqa: E501

        :param tx_hash: The tx_hash of this AuthChainElement.  # noqa: E501
        :type tx_hash: str
        """

        self._tx_hash = tx_hash

    @property
    def content_hash(self):
        """Gets the content_hash of this AuthChainElement.  # noqa: E501

        Content hash of the remote registry, either a SHA256 hash of an HTTPS Publication output or an IPFS CID  # noqa: E501

        :return: The content_hash of this AuthChainElement.  # noqa: E501
        :rtype: str
        """
        return self._content_hash

    @content_hash.setter
    def content_hash(self, content_hash):
        """Sets the content_hash of this AuthChainElement.

        Content hash of the remote registry, either a SHA256 hash of an HTTPS Publication output or an IPFS CID  # noqa: E501

        :param content_hash: The content_hash of this AuthChainElement.  # noqa: E501
        :type content_hash: str
        """

        self._content_hash = content_hash

    @property
    def uris(self):
        """Gets the uris of this AuthChainElement.  # noqa: E501

        URIs of BCMR publication OP_RETURN  # noqa: E501

        :return: The uris of this AuthChainElement.  # noqa: E501
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """Sets the uris of this AuthChainElement.

        URIs of BCMR publication OP_RETURN  # noqa: E501

        :param uris: The uris of this AuthChainElement.  # noqa: E501
        :type uris: list[str]
        """

        self._uris = uris

    @property
    def https_url(self):
        """Gets the https_url of this AuthChainElement.  # noqa: E501

        URL to fetch the registry contents from  # noqa: E501

        :return: The https_url of this AuthChainElement.  # noqa: E501
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        """Sets the https_url of this AuthChainElement.

        URL to fetch the registry contents from  # noqa: E501

        :param https_url: The https_url of this AuthChainElement.  # noqa: E501
        :type https_url: str
        """

        self._https_url = https_url

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
        if not isinstance(other, AuthChainElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthChainElement):
            return True

        return self.to_dict() != other.to_dict()
