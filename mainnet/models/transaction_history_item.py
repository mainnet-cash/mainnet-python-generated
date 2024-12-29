# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.6.0
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
        'inputs': 'list[InOutput]',
        'outputs': 'list[InOutput]',
        'blockheight': 'float',
        'timestamp': 'str',
        'hash': 'str',
        'size': 'float',
        'fee': 'float',
        'balance': 'float',
        'value_change': 'float',
        'token_amount_changes': 'list[TokenAmountChange]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'outputs': 'outputs',
        'blockheight': 'blockheight',
        'timestamp': 'timestamp',
        'hash': 'hash',
        'size': 'size',
        'fee': 'fee',
        'balance': 'balance',
        'value_change': 'valueChange',
        'token_amount_changes': 'tokenAmountChanges'
    }

    def __init__(self, inputs=None, outputs=None, blockheight=None, timestamp=None, hash=None, size=None, fee=None, balance=None, value_change=None, token_amount_changes=None, local_vars_configuration=None):  # noqa: E501
        """TransactionHistoryItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inputs = None
        self._outputs = None
        self._blockheight = None
        self._timestamp = None
        self._hash = None
        self._size = None
        self._fee = None
        self._balance = None
        self._value_change = None
        self._token_amount_changes = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if blockheight is not None:
            self.blockheight = blockheight
        self.timestamp = timestamp
        if hash is not None:
            self.hash = hash
        if size is not None:
            self.size = size
        if fee is not None:
            self.fee = fee
        if balance is not None:
            self.balance = balance
        if value_change is not None:
            self.value_change = value_change
        if token_amount_changes is not None:
            self.token_amount_changes = token_amount_changes

    @property
    def inputs(self):
        """Gets the inputs of this TransactionHistoryItem.  # noqa: E501


        :return: The inputs of this TransactionHistoryItem.  # noqa: E501
        :rtype: list[InOutput]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TransactionHistoryItem.


        :param inputs: The inputs of this TransactionHistoryItem.  # noqa: E501
        :type inputs: list[InOutput]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this TransactionHistoryItem.  # noqa: E501


        :return: The outputs of this TransactionHistoryItem.  # noqa: E501
        :rtype: list[InOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TransactionHistoryItem.


        :param outputs: The outputs of this TransactionHistoryItem.  # noqa: E501
        :type outputs: list[InOutput]
        """

        self._outputs = outputs

    @property
    def blockheight(self):
        """Gets the blockheight of this TransactionHistoryItem.  # noqa: E501

        The blockheight of transaction  # noqa: E501

        :return: The blockheight of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._blockheight

    @blockheight.setter
    def blockheight(self, blockheight):
        """Sets the blockheight of this TransactionHistoryItem.

        The blockheight of transaction  # noqa: E501

        :param blockheight: The blockheight of this TransactionHistoryItem.  # noqa: E501
        :type blockheight: float
        """

        self._blockheight = blockheight

    @property
    def timestamp(self):
        """Gets the timestamp of this TransactionHistoryItem.  # noqa: E501

        The timestamp of transaction, undefined if unconfirmed  # noqa: E501

        :return: The timestamp of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TransactionHistoryItem.

        The timestamp of transaction, undefined if unconfirmed  # noqa: E501

        :param timestamp: The timestamp of this TransactionHistoryItem.  # noqa: E501
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def hash(self):
        """Gets the hash of this TransactionHistoryItem.  # noqa: E501

        The hash of the transaction  # noqa: E501

        :return: The hash of this TransactionHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this TransactionHistoryItem.

        The hash of the transaction  # noqa: E501

        :param hash: The hash of this TransactionHistoryItem.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def size(self):
        """Gets the size of this TransactionHistoryItem.  # noqa: E501

        The size of the transaction  # noqa: E501

        :return: The size of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TransactionHistoryItem.

        The size of the transaction  # noqa: E501

        :param size: The size of this TransactionHistoryItem.  # noqa: E501
        :type size: float
        """

        self._size = size

    @property
    def fee(self):
        """Gets the fee of this TransactionHistoryItem.  # noqa: E501

        Transaction fee  # noqa: E501

        :return: The fee of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this TransactionHistoryItem.

        Transaction fee  # noqa: E501

        :param fee: The fee of this TransactionHistoryItem.  # noqa: E501
        :type fee: float
        """

        self._fee = fee

    @property
    def balance(self):
        """Gets the balance of this TransactionHistoryItem.  # noqa: E501

        A running balance, in units  # noqa: E501

        :return: The balance of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this TransactionHistoryItem.

        A running balance, in units  # noqa: E501

        :param balance: The balance of this TransactionHistoryItem.  # noqa: E501
        :type balance: float
        """

        self._balance = balance

    @property
    def value_change(self):
        """Gets the value_change of this TransactionHistoryItem.  # noqa: E501

        Change of value in the transaction, in units  # noqa: E501

        :return: The value_change of this TransactionHistoryItem.  # noqa: E501
        :rtype: float
        """
        return self._value_change

    @value_change.setter
    def value_change(self, value_change):
        """Sets the value_change of this TransactionHistoryItem.

        Change of value in the transaction, in units  # noqa: E501

        :param value_change: The value_change of this TransactionHistoryItem.  # noqa: E501
        :type value_change: float
        """

        self._value_change = value_change

    @property
    def token_amount_changes(self):
        """Gets the token_amount_changes of this TransactionHistoryItem.  # noqa: E501


        :return: The token_amount_changes of this TransactionHistoryItem.  # noqa: E501
        :rtype: list[TokenAmountChange]
        """
        return self._token_amount_changes

    @token_amount_changes.setter
    def token_amount_changes(self, token_amount_changes):
        """Sets the token_amount_changes of this TransactionHistoryItem.


        :param token_amount_changes: The token_amount_changes of this TransactionHistoryItem.  # noqa: E501
        :type token_amount_changes: list[TokenAmountChange]
        """

        self._token_amount_changes = token_amount_changes

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
