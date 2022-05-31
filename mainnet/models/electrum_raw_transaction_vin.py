# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.5.2
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ElectrumRawTransactionVin(object):
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
        'script_sig': 'ElectrumRawTransactionScriptSig',
        'sequence': 'float',
        'txid': 'str',
        'vout': 'float',
        'value': 'float',
        'address': 'str'
    }

    attribute_map = {
        'script_sig': 'scriptSig',
        'sequence': 'sequence',
        'txid': 'txid',
        'vout': 'vout',
        'value': 'value',
        'address': 'address'
    }

    def __init__(self, script_sig=None, sequence=None, txid=None, vout=None, value=None, address=None, local_vars_configuration=None):  # noqa: E501
        """ElectrumRawTransactionVin - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._script_sig = None
        self._sequence = None
        self._txid = None
        self._vout = None
        self._value = None
        self._address = None
        self.discriminator = None

        if script_sig is not None:
            self.script_sig = script_sig
        if sequence is not None:
            self.sequence = sequence
        if txid is not None:
            self.txid = txid
        if vout is not None:
            self.vout = vout
        if value is not None:
            self.value = value
        if address is not None:
            self.address = address

    @property
    def script_sig(self):
        """Gets the script_sig of this ElectrumRawTransactionVin.  # noqa: E501


        :return: The script_sig of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: ElectrumRawTransactionScriptSig
        """
        return self._script_sig

    @script_sig.setter
    def script_sig(self, script_sig):
        """Sets the script_sig of this ElectrumRawTransactionVin.


        :param script_sig: The script_sig of this ElectrumRawTransactionVin.  # noqa: E501
        :type script_sig: ElectrumRawTransactionScriptSig
        """

        self._script_sig = script_sig

    @property
    def sequence(self):
        """Gets the sequence of this ElectrumRawTransactionVin.  # noqa: E501


        :return: The sequence of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: float
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this ElectrumRawTransactionVin.


        :param sequence: The sequence of this ElectrumRawTransactionVin.  # noqa: E501
        :type sequence: float
        """

        self._sequence = sequence

    @property
    def txid(self):
        """Gets the txid of this ElectrumRawTransactionVin.  # noqa: E501


        :return: The txid of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this ElectrumRawTransactionVin.


        :param txid: The txid of this ElectrumRawTransactionVin.  # noqa: E501
        :type txid: str
        """

        self._txid = txid

    @property
    def vout(self):
        """Gets the vout of this ElectrumRawTransactionVin.  # noqa: E501


        :return: The vout of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: float
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this ElectrumRawTransactionVin.


        :param vout: The vout of this ElectrumRawTransactionVin.  # noqa: E501
        :type vout: float
        """

        self._vout = vout

    @property
    def value(self):
        """Gets the value of this ElectrumRawTransactionVin.  # noqa: E501

        optional extention by mainnet.cash  # noqa: E501

        :return: The value of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ElectrumRawTransactionVin.

        optional extention by mainnet.cash  # noqa: E501

        :param value: The value of this ElectrumRawTransactionVin.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def address(self):
        """Gets the address of this ElectrumRawTransactionVin.  # noqa: E501

        optional extention by mainnet.cash  # noqa: E501

        :return: The address of this ElectrumRawTransactionVin.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ElectrumRawTransactionVin.

        optional extention by mainnet.cash  # noqa: E501

        :param address: The address of this ElectrumRawTransactionVin.  # noqa: E501
        :type address: str
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
        if not isinstance(other, ElectrumRawTransactionVin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectrumRawTransactionVin):
            return True

        return self.to_dict() != other.to_dict()
