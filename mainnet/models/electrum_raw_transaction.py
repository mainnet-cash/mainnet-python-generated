# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.7.14
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ElectrumRawTransaction(object):
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
        'blockhash': 'str',
        'blocktime': 'float',
        'confirmations': 'float',
        'hash': 'str',
        'hex': 'str',
        'locktime': 'float',
        'size': 'float',
        'time': 'float',
        'txid': 'str',
        'version': 'float',
        'vin': 'list[ElectrumRawTransactionVin]',
        'vout': 'list[ElectrumRawTransactionVout]'
    }

    attribute_map = {
        'blockhash': 'blockhash',
        'blocktime': 'blocktime',
        'confirmations': 'confirmations',
        'hash': 'hash',
        'hex': 'hex',
        'locktime': 'locktime',
        'size': 'size',
        'time': 'time',
        'txid': 'txid',
        'version': 'version',
        'vin': 'vin',
        'vout': 'vout'
    }

    def __init__(self, blockhash=None, blocktime=None, confirmations=None, hash=None, hex=None, locktime=None, size=None, time=None, txid=None, version=None, vin=None, vout=None, local_vars_configuration=None):  # noqa: E501
        """ElectrumRawTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._blockhash = None
        self._blocktime = None
        self._confirmations = None
        self._hash = None
        self._hex = None
        self._locktime = None
        self._size = None
        self._time = None
        self._txid = None
        self._version = None
        self._vin = None
        self._vout = None
        self.discriminator = None

        if blockhash is not None:
            self.blockhash = blockhash
        if blocktime is not None:
            self.blocktime = blocktime
        if confirmations is not None:
            self.confirmations = confirmations
        if hash is not None:
            self.hash = hash
        if hex is not None:
            self.hex = hex
        if locktime is not None:
            self.locktime = locktime
        if size is not None:
            self.size = size
        if time is not None:
            self.time = time
        if txid is not None:
            self.txid = txid
        if version is not None:
            self.version = version
        if vin is not None:
            self.vin = vin
        if vout is not None:
            self.vout = vout

    @property
    def blockhash(self):
        """Gets the blockhash of this ElectrumRawTransaction.  # noqa: E501


        :return: The blockhash of this ElectrumRawTransaction.  # noqa: E501
        :rtype: str
        """
        return self._blockhash

    @blockhash.setter
    def blockhash(self, blockhash):
        """Sets the blockhash of this ElectrumRawTransaction.


        :param blockhash: The blockhash of this ElectrumRawTransaction.  # noqa: E501
        :type blockhash: str
        """

        self._blockhash = blockhash

    @property
    def blocktime(self):
        """Gets the blocktime of this ElectrumRawTransaction.  # noqa: E501


        :return: The blocktime of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._blocktime

    @blocktime.setter
    def blocktime(self, blocktime):
        """Sets the blocktime of this ElectrumRawTransaction.


        :param blocktime: The blocktime of this ElectrumRawTransaction.  # noqa: E501
        :type blocktime: float
        """

        self._blocktime = blocktime

    @property
    def confirmations(self):
        """Gets the confirmations of this ElectrumRawTransaction.  # noqa: E501


        :return: The confirmations of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this ElectrumRawTransaction.


        :param confirmations: The confirmations of this ElectrumRawTransaction.  # noqa: E501
        :type confirmations: float
        """

        self._confirmations = confirmations

    @property
    def hash(self):
        """Gets the hash of this ElectrumRawTransaction.  # noqa: E501


        :return: The hash of this ElectrumRawTransaction.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ElectrumRawTransaction.


        :param hash: The hash of this ElectrumRawTransaction.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def hex(self):
        """Gets the hex of this ElectrumRawTransaction.  # noqa: E501


        :return: The hex of this ElectrumRawTransaction.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this ElectrumRawTransaction.


        :param hex: The hex of this ElectrumRawTransaction.  # noqa: E501
        :type hex: str
        """

        self._hex = hex

    @property
    def locktime(self):
        """Gets the locktime of this ElectrumRawTransaction.  # noqa: E501


        :return: The locktime of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._locktime

    @locktime.setter
    def locktime(self, locktime):
        """Sets the locktime of this ElectrumRawTransaction.


        :param locktime: The locktime of this ElectrumRawTransaction.  # noqa: E501
        :type locktime: float
        """

        self._locktime = locktime

    @property
    def size(self):
        """Gets the size of this ElectrumRawTransaction.  # noqa: E501


        :return: The size of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ElectrumRawTransaction.


        :param size: The size of this ElectrumRawTransaction.  # noqa: E501
        :type size: float
        """

        self._size = size

    @property
    def time(self):
        """Gets the time of this ElectrumRawTransaction.  # noqa: E501


        :return: The time of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ElectrumRawTransaction.


        :param time: The time of this ElectrumRawTransaction.  # noqa: E501
        :type time: float
        """

        self._time = time

    @property
    def txid(self):
        """Gets the txid of this ElectrumRawTransaction.  # noqa: E501


        :return: The txid of this ElectrumRawTransaction.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this ElectrumRawTransaction.


        :param txid: The txid of this ElectrumRawTransaction.  # noqa: E501
        :type txid: str
        """

        self._txid = txid

    @property
    def version(self):
        """Gets the version of this ElectrumRawTransaction.  # noqa: E501


        :return: The version of this ElectrumRawTransaction.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ElectrumRawTransaction.


        :param version: The version of this ElectrumRawTransaction.  # noqa: E501
        :type version: float
        """

        self._version = version

    @property
    def vin(self):
        """Gets the vin of this ElectrumRawTransaction.  # noqa: E501


        :return: The vin of this ElectrumRawTransaction.  # noqa: E501
        :rtype: list[ElectrumRawTransactionVin]
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this ElectrumRawTransaction.


        :param vin: The vin of this ElectrumRawTransaction.  # noqa: E501
        :type vin: list[ElectrumRawTransactionVin]
        """

        self._vin = vin

    @property
    def vout(self):
        """Gets the vout of this ElectrumRawTransaction.  # noqa: E501


        :return: The vout of this ElectrumRawTransaction.  # noqa: E501
        :rtype: list[ElectrumRawTransactionVout]
        """
        return self._vout

    @vout.setter
    def vout(self, vout):
        """Sets the vout of this ElectrumRawTransaction.


        :param vout: The vout of this ElectrumRawTransaction.  # noqa: E501
        :type vout: list[ElectrumRawTransactionVout]
        """

        self._vout = vout

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
        if not isinstance(other, ElectrumRawTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElectrumRawTransaction):
            return True

        return self.to_dict() != other.to_dict()
