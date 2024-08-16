# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.4.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class Utxo(object):
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
        'vout': 'float',
        'txid': 'str',
        'satoshis': 'float',
        'token': 'Token'
    }

    attribute_map = {
        'vout': 'vout',
        'txid': 'txid',
        'satoshis': 'satoshis',
        'token': 'token'
    }

    def __init__(self, vout=None, txid=None, satoshis=None, token=None, local_vars_configuration=None):  # noqa: E501
        """Utxo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vout = None
        self._txid = None
        self._satoshis = None
        self._token = None
        self.discriminator = None

        self.vout = vout
        self.txid = txid
        self.satoshis = satoshis
        self.token = token

    @property
    def vout(self):
        """Gets the vout of this Utxo.  # noqa: E501


        :return: The vout of this Utxo.  # noqa: E501
        :rtype: float
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this Utxo.


        :param vout: The vout of this Utxo.  # noqa: E501
        :type vout: float
        """
        if self.local_vars_configuration.client_side_validation and vout is None:  # noqa: E501
            raise ValueError("Invalid value for `vout`, must not be `None`")  # noqa: E501

        self._vout = vout

    @property
    def txid(self):
        """Gets the txid of this Utxo.  # noqa: E501

        The hash of a transaction  # noqa: E501

        :return: The txid of this Utxo.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this Utxo.

        The hash of a transaction  # noqa: E501

        :param txid: The txid of this Utxo.  # noqa: E501
        :type txid: str
        """
        if self.local_vars_configuration.client_side_validation and txid is None:  # noqa: E501
            raise ValueError("Invalid value for `txid`, must not be `None`")  # noqa: E501

        self._txid = txid

    @property
    def satoshis(self):
        """Gets the satoshis of this Utxo.  # noqa: E501


        :return: The satoshis of this Utxo.  # noqa: E501
        :rtype: float
        """
        return self._satoshis

    @satoshis.setter
    def satoshis(self, satoshis):
        """Sets the satoshis of this Utxo.


        :param satoshis: The satoshis of this Utxo.  # noqa: E501
        :type satoshis: float
        """
        if self.local_vars_configuration.client_side_validation and satoshis is None:  # noqa: E501
            raise ValueError("Invalid value for `satoshis`, must not be `None`")  # noqa: E501

        self._satoshis = satoshis

    @property
    def token(self):
        """Gets the token of this Utxo.  # noqa: E501


        :return: The token of this Utxo.  # noqa: E501
        :rtype: Token
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Utxo.


        :param token: The token of this Utxo.  # noqa: E501
        :type token: Token
        """

        self._token = token

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
        if not isinstance(other, Utxo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Utxo):
            return True

        return self.to_dict() != other.to_dict()
