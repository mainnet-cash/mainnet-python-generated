# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.3.7
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class WalletInfo(object):
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
        'cashaddr': 'str',
        'tokenaddr': 'str',
        'is_testnet': 'bool',
        'name': 'str',
        'public_key': 'str',
        'public_key_hash': 'str',
        'private_key': 'str',
        'private_key_wif': 'str',
        'seed': 'str',
        'derivation_path': 'str',
        'wallet_id': 'str',
        'wallet_db_entry': 'str'
    }

    attribute_map = {
        'cashaddr': 'cashaddr',
        'tokenaddr': 'tokenaddr',
        'is_testnet': 'isTestnet',
        'name': 'name',
        'public_key': 'publicKey',
        'public_key_hash': 'publicKeyHash',
        'private_key': 'privateKey',
        'private_key_wif': 'privateKeyWif',
        'seed': 'seed',
        'derivation_path': 'derivationPath',
        'wallet_id': 'walletId',
        'wallet_db_entry': 'walletDbEntry'
    }

    def __init__(self, cashaddr=None, tokenaddr=None, is_testnet=None, name=None, public_key=None, public_key_hash=None, private_key=None, private_key_wif=None, seed=None, derivation_path=None, wallet_id=None, wallet_db_entry=None, local_vars_configuration=None):  # noqa: E501
        """WalletInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cashaddr = None
        self._tokenaddr = None
        self._is_testnet = None
        self._name = None
        self._public_key = None
        self._public_key_hash = None
        self._private_key = None
        self._private_key_wif = None
        self._seed = None
        self._derivation_path = None
        self._wallet_id = None
        self._wallet_db_entry = None
        self.discriminator = None

        if cashaddr is not None:
            self.cashaddr = cashaddr
        if tokenaddr is not None:
            self.tokenaddr = tokenaddr
        if is_testnet is not None:
            self.is_testnet = is_testnet
        if name is not None:
            self.name = name
        if public_key is not None:
            self.public_key = public_key
        if public_key_hash is not None:
            self.public_key_hash = public_key_hash
        if private_key is not None:
            self.private_key = private_key
        if private_key_wif is not None:
            self.private_key_wif = private_key_wif
        if seed is not None:
            self.seed = seed
        if derivation_path is not None:
            self.derivation_path = derivation_path
        if wallet_id is not None:
            self.wallet_id = wallet_id
        if wallet_db_entry is not None:
            self.wallet_db_entry = wallet_db_entry

    @property
    def cashaddr(self):
        """Gets the cashaddr of this WalletInfo.  # noqa: E501


        :return: The cashaddr of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this WalletInfo.


        :param cashaddr: The cashaddr of this WalletInfo.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def tokenaddr(self):
        """Gets the tokenaddr of this WalletInfo.  # noqa: E501


        :return: The tokenaddr of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._tokenaddr

    @tokenaddr.setter
    def tokenaddr(self, tokenaddr):
        """Sets the tokenaddr of this WalletInfo.


        :param tokenaddr: The tokenaddr of this WalletInfo.  # noqa: E501
        :type tokenaddr: str
        """

        self._tokenaddr = tokenaddr

    @property
    def is_testnet(self):
        """Gets the is_testnet of this WalletInfo.  # noqa: E501

        Whether the agreed value of the network is zero. True for all non-mainnet networks.  # noqa: E501

        :return: The is_testnet of this WalletInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_testnet

    @is_testnet.setter
    def is_testnet(self, is_testnet):
        """Sets the is_testnet of this WalletInfo.

        Whether the agreed value of the network is zero. True for all non-mainnet networks.  # noqa: E501

        :param is_testnet: The is_testnet of this WalletInfo.  # noqa: E501
        :type is_testnet: bool
        """

        self._is_testnet = is_testnet

    @property
    def name(self):
        """Gets the name of this WalletInfo.  # noqa: E501


        :return: The name of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WalletInfo.


        :param name: The name of this WalletInfo.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this WalletInfo.  # noqa: E501


        :return: The public_key of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this WalletInfo.


        :param public_key: The public_key of this WalletInfo.  # noqa: E501
        :type public_key: str
        """

        self._public_key = public_key

    @property
    def public_key_hash(self):
        """Gets the public_key_hash of this WalletInfo.  # noqa: E501


        :return: The public_key_hash of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, public_key_hash):
        """Sets the public_key_hash of this WalletInfo.


        :param public_key_hash: The public_key_hash of this WalletInfo.  # noqa: E501
        :type public_key_hash: str
        """

        self._public_key_hash = public_key_hash

    @property
    def private_key(self):
        """Gets the private_key of this WalletInfo.  # noqa: E501


        :return: The private_key of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this WalletInfo.


        :param private_key: The private_key of this WalletInfo.  # noqa: E501
        :type private_key: str
        """

        self._private_key = private_key

    @property
    def private_key_wif(self):
        """Gets the private_key_wif of this WalletInfo.  # noqa: E501


        :return: The private_key_wif of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._private_key_wif

    @private_key_wif.setter
    def private_key_wif(self, private_key_wif):
        """Sets the private_key_wif of this WalletInfo.


        :param private_key_wif: The private_key_wif of this WalletInfo.  # noqa: E501
        :type private_key_wif: str
        """

        self._private_key_wif = private_key_wif

    @property
    def seed(self):
        """Gets the seed of this WalletInfo.  # noqa: E501


        :return: The seed of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this WalletInfo.


        :param seed: The seed of this WalletInfo.  # noqa: E501
        :type seed: str
        """

        self._seed = seed

    @property
    def derivation_path(self):
        """Gets the derivation_path of this WalletInfo.  # noqa: E501


        :return: The derivation_path of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._derivation_path

    @derivation_path.setter
    def derivation_path(self, derivation_path):
        """Sets the derivation_path of this WalletInfo.


        :param derivation_path: The derivation_path of this WalletInfo.  # noqa: E501
        :type derivation_path: str
        """

        self._derivation_path = derivation_path

    @property
    def wallet_id(self):
        """Gets the wallet_id of this WalletInfo.  # noqa: E501


        :return: The wallet_id of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this WalletInfo.


        :param wallet_id: The wallet_id of this WalletInfo.  # noqa: E501
        :type wallet_id: str
        """

        self._wallet_id = wallet_id

    @property
    def wallet_db_entry(self):
        """Gets the wallet_db_entry of this WalletInfo.  # noqa: E501

        The serialized form with private information  # noqa: E501

        :return: The wallet_db_entry of this WalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._wallet_db_entry

    @wallet_db_entry.setter
    def wallet_db_entry(self, wallet_db_entry):
        """Sets the wallet_db_entry of this WalletInfo.

        The serialized form with private information  # noqa: E501

        :param wallet_db_entry: The wallet_db_entry of this WalletInfo.  # noqa: E501
        :type wallet_db_entry: str
        """

        self._wallet_db_entry = wallet_db_entry

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
        if not isinstance(other, WalletInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WalletInfo):
            return True

        return self.to_dict() != other.to_dict()
