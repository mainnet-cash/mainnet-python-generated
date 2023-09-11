# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class TransactionHistoryItem(object):
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
        'to': 'str',
        '_from': 'str',
        'unit': 'UnitType',
        'index': 'float',
        'blockheight': 'float',
        'txn': 'str',
        'tx_id': 'str',
        'value': 'float',
        'fee': 'float',
        'balance': 'float'
    }

    attribute_map = {
        'to': 'to',
        '_from': 'from',
        'unit': 'unit',
        'index': 'index',
        'blockheight': 'blockheight',
        'txn': 'txn',
        'tx_id': 'txId',
        'value': 'value',
        'fee': 'fee',
        'balance': 'balance'
    }

    def __init__(self, to=None, _from=None, unit=None, index=None, blockheight=None, txn=None, tx_id=None, value=None, fee=None, balance=None, local_vars_configuration=None):  # noqa: E501
        """TransactionHistoryItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self.__from = None
        self._unit = None
        self._index = None
        self._blockheight = None
        self._txn = None
        self._tx_id = None
        self._value = None
        self._fee = None
        self._balance = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if _from is not None:
            self._from = _from
        if unit is not None:
            self.unit = unit
        if index is not None:
            self.index = index
        if blockheight is not None:
            self.blockheight = blockheight
        if txn is not None:
            self.txn = txn
        if tx_id is not None:
            self.tx_id = tx_id
        if value is not None:
            self.value = value
        if fee is not None:
            self.fee = fee
        if balance is not None:
            self.balance = balance

    @property
    def to(self):
        """Gets the to of this TransactionHistoryItem.  # noqa: E501

        cashaddr of the receiving cash address.  # noqa: E501

        :return: The to of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TransactionHistoryItem.

        cashaddr of the receiving cash address.  # noqa: E501

        :param to: The to of this TransactionHistoryItem.  # noqa: E501
        :type to: str
        """

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this TransactionHistoryItem.  # noqa: E501

        cashaddr of the sending cash address.  # noqa: E501

        :return: The _from of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TransactionHistoryItem.

        cashaddr of the sending cash address.  # noqa: E501

        :param _from: The _from of this TransactionHistoryItem.  # noqa: E501
        :type _from: str
        """

        self.__from = _from

    @property
    def unit(self):
        """Gets the unit of this TransactionHistoryItem.  # noqa: E501


        :return: The unit of this TransactionHistoryItem.  # noqa: E501
        :rtype: UnitType
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TransactionHistoryItem.


        :param unit: The unit of this TransactionHistoryItem.  # noqa: E501
        :type unit: UnitType
        """

        self._unit = unit

    @property
    def index(self):
        """Gets the index of this TransactionHistoryItem.  # noqa: E501

        the index of the input or output in the transaction  # noqa: E501

        :return: The index of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this TransactionHistoryItem.

        the index of the input or output in the transaction  # noqa: E501

        :param index: The index of this TransactionHistoryItem.  # noqa: E501
        :type index: float
        """

        self._index = index

    @property
    def blockheight(self):
        """Gets the blockheight of this TransactionHistoryItem.  # noqa: E501

        the blockheight of transaction  # noqa: E501

        :return: The blockheight of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._blockheight

    @blockheight.setter
    def blockheight(self, blockheight):
        """Sets the blockheight of this TransactionHistoryItem.

        the blockheight of transaction  # noqa: E501

        :param blockheight: The blockheight of this TransactionHistoryItem.  # noqa: E501
        :type blockheight: float
        """

        self._blockheight = blockheight

    @property
    def txn(self):
        """Gets the txn of this TransactionHistoryItem.  # noqa: E501

        The hash of the transaction  # noqa: E501

        :return: The txn of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._txn

    @txn.setter
    def txn(self, txn):
        """Sets the txn of this TransactionHistoryItem.

        The hash of the transaction  # noqa: E501

        :param txn: The txn of this TransactionHistoryItem.  # noqa: E501
        :type txn: str
        """

        self._txn = txn

    @property
    def tx_id(self):
        """Gets the tx_id of this TransactionHistoryItem.  # noqa: E501

        a unique identifier for the sub-transaction  # noqa: E501

        :return: The tx_id of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this TransactionHistoryItem.

        a unique identifier for the sub-transaction  # noqa: E501

        :param tx_id: The tx_id of this TransactionHistoryItem.  # noqa: E501
        :type tx_id: str
        """

        self._tx_id = tx_id

    @property
    def value(self):
        """Gets the value of this TransactionHistoryItem.  # noqa: E501

        The amount of the transaction, in the unit provided, with respect to the wallet provided.  # noqa: E501

        :return: The value of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransactionHistoryItem.

        The amount of the transaction, in the unit provided, with respect to the wallet provided.  # noqa: E501

        :param value: The value of this TransactionHistoryItem.  # noqa: E501
        :type value: float
        """

        self._value = value

    @property
    def fee(self):
        """Gets the fee of this TransactionHistoryItem.  # noqa: E501

        The amount paid, if any, by the wallet for the transaction (incoming tranactions are \"free\")  # noqa: E501

        :return: The fee of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this TransactionHistoryItem.

        The amount paid, if any, by the wallet for the transaction (incoming tranactions are \"free\")  # noqa: E501

        :param fee: The fee of this TransactionHistoryItem.  # noqa: E501
        :type fee: float
        """

        self._fee = fee

    @property
    def balance(self):
        """Gets the balance of this TransactionHistoryItem.  # noqa: E501

        A running balance  # noqa: E501

        :return: The balance of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this TransactionHistoryItem.

        A running balance  # noqa: E501

        :param balance: The balance of this TransactionHistoryItem.  # noqa: E501
        :type balance: float
        """

        self._balance = balance

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
        if not isinstance(other, TransactionHistoryItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionHistoryItem):
            return True

        return self.to_dict() != other.to_dict()
