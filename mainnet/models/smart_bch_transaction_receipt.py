# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.0.15
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchTransactionReceipt(object):
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
        'contract_address': 'str',
        'transaction_index': 'float',
        'root': 'str',
        'gas_used': 'str',
        'logs_bloom': 'str',
        'block_hash': 'str',
        'transaction_hash': 'str',
        'logs': 'list[object]',
        'block_number': 'float',
        'confirmations': 'float',
        'cumulative_gas_used': 'str',
        'effective_gas_price': 'str',
        'byzantium': 'bool',
        'type': 'float',
        'status': 'float'
    }

    attribute_map = {
        'to': 'to',
        '_from': 'from',
        'contract_address': 'contractAddress',
        'transaction_index': 'transactionIndex',
        'root': 'root',
        'gas_used': 'gasUsed',
        'logs_bloom': 'logsBloom',
        'block_hash': 'blockHash',
        'transaction_hash': 'transactionHash',
        'logs': 'logs',
        'block_number': 'blockNumber',
        'confirmations': 'confirmations',
        'cumulative_gas_used': 'cumulativeGasUsed',
        'effective_gas_price': 'effectiveGasPrice',
        'byzantium': 'byzantium',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, to=None, _from=None, contract_address=None, transaction_index=None, root=None, gas_used=None, logs_bloom=None, block_hash=None, transaction_hash=None, logs=None, block_number=None, confirmations=None, cumulative_gas_used=None, effective_gas_price=None, byzantium=None, type=None, status=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchTransactionReceipt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self.__from = None
        self._contract_address = None
        self._transaction_index = None
        self._root = None
        self._gas_used = None
        self._logs_bloom = None
        self._block_hash = None
        self._transaction_hash = None
        self._logs = None
        self._block_number = None
        self._confirmations = None
        self._cumulative_gas_used = None
        self._effective_gas_price = None
        self._byzantium = None
        self._type = None
        self._status = None
        self.discriminator = None

        self.to = to
        self._from = _from
        self.contract_address = contract_address
        self.transaction_index = transaction_index
        if root is not None:
            self.root = root
        self.gas_used = gas_used
        self.logs_bloom = logs_bloom
        self.block_hash = block_hash
        self.transaction_hash = transaction_hash
        self.logs = logs
        self.block_number = block_number
        self.confirmations = confirmations
        self.cumulative_gas_used = cumulative_gas_used
        self.effective_gas_price = effective_gas_price
        self.byzantium = byzantium
        self.type = type
        if status is not None:
            self.status = status

    @property
    def to(self):
        """Gets the to of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The to of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SmartBchTransactionReceipt.


        :param to: The to of this SmartBchTransactionReceipt.  # noqa: E501
        :type to: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The _from of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SmartBchTransactionReceipt.


        :param _from: The _from of this SmartBchTransactionReceipt.  # noqa: E501
        :type _from: str
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def contract_address(self):
        """Gets the contract_address of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The contract_address of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this SmartBchTransactionReceipt.


        :param contract_address: The contract_address of this SmartBchTransactionReceipt.  # noqa: E501
        :type contract_address: str
        """
        if self.local_vars_configuration.client_side_validation and contract_address is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

    @property
    def transaction_index(self):
        """Gets the transaction_index of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The transaction_index of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: float
        """
        return self._transaction_index

    @transaction_index.setter
    def transaction_index(self, transaction_index):
        """Sets the transaction_index of this SmartBchTransactionReceipt.


        :param transaction_index: The transaction_index of this SmartBchTransactionReceipt.  # noqa: E501
        :type transaction_index: float
        """
        if self.local_vars_configuration.client_side_validation and transaction_index is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_index`, must not be `None`")  # noqa: E501

        self._transaction_index = transaction_index

    @property
    def root(self):
        """Gets the root of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The root of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this SmartBchTransactionReceipt.


        :param root: The root of this SmartBchTransactionReceipt.  # noqa: E501
        :type root: str
        """

        self._root = root

    @property
    def gas_used(self):
        """Gets the gas_used of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The gas_used of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._gas_used

    @gas_used.setter
    def gas_used(self, gas_used):
        """Sets the gas_used of this SmartBchTransactionReceipt.


        :param gas_used: The gas_used of this SmartBchTransactionReceipt.  # noqa: E501
        :type gas_used: str
        """
        if self.local_vars_configuration.client_side_validation and gas_used is None:  # noqa: E501
            raise ValueError("Invalid value for `gas_used`, must not be `None`")  # noqa: E501

        self._gas_used = gas_used

    @property
    def logs_bloom(self):
        """Gets the logs_bloom of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The logs_bloom of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._logs_bloom

    @logs_bloom.setter
    def logs_bloom(self, logs_bloom):
        """Sets the logs_bloom of this SmartBchTransactionReceipt.


        :param logs_bloom: The logs_bloom of this SmartBchTransactionReceipt.  # noqa: E501
        :type logs_bloom: str
        """
        if self.local_vars_configuration.client_side_validation and logs_bloom is None:  # noqa: E501
            raise ValueError("Invalid value for `logs_bloom`, must not be `None`")  # noqa: E501

        self._logs_bloom = logs_bloom

    @property
    def block_hash(self):
        """Gets the block_hash of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The block_hash of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._block_hash

    @block_hash.setter
    def block_hash(self, block_hash):
        """Sets the block_hash of this SmartBchTransactionReceipt.


        :param block_hash: The block_hash of this SmartBchTransactionReceipt.  # noqa: E501
        :type block_hash: str
        """
        if self.local_vars_configuration.client_side_validation and block_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `block_hash`, must not be `None`")  # noqa: E501

        self._block_hash = block_hash

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The transaction_hash of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this SmartBchTransactionReceipt.


        :param transaction_hash: The transaction_hash of this SmartBchTransactionReceipt.  # noqa: E501
        :type transaction_hash: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def logs(self):
        """Gets the logs of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The logs of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: list[object]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this SmartBchTransactionReceipt.


        :param logs: The logs of this SmartBchTransactionReceipt.  # noqa: E501
        :type logs: list[object]
        """
        if self.local_vars_configuration.client_side_validation and logs is None:  # noqa: E501
            raise ValueError("Invalid value for `logs`, must not be `None`")  # noqa: E501

        self._logs = logs

    @property
    def block_number(self):
        """Gets the block_number of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The block_number of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: float
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number):
        """Sets the block_number of this SmartBchTransactionReceipt.


        :param block_number: The block_number of this SmartBchTransactionReceipt.  # noqa: E501
        :type block_number: float
        """
        if self.local_vars_configuration.client_side_validation and block_number is None:  # noqa: E501
            raise ValueError("Invalid value for `block_number`, must not be `None`")  # noqa: E501

        self._block_number = block_number

    @property
    def confirmations(self):
        """Gets the confirmations of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The confirmations of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: float
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations):
        """Sets the confirmations of this SmartBchTransactionReceipt.


        :param confirmations: The confirmations of this SmartBchTransactionReceipt.  # noqa: E501
        :type confirmations: float
        """
        if self.local_vars_configuration.client_side_validation and confirmations is None:  # noqa: E501
            raise ValueError("Invalid value for `confirmations`, must not be `None`")  # noqa: E501

        self._confirmations = confirmations

    @property
    def cumulative_gas_used(self):
        """Gets the cumulative_gas_used of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The cumulative_gas_used of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._cumulative_gas_used

    @cumulative_gas_used.setter
    def cumulative_gas_used(self, cumulative_gas_used):
        """Sets the cumulative_gas_used of this SmartBchTransactionReceipt.


        :param cumulative_gas_used: The cumulative_gas_used of this SmartBchTransactionReceipt.  # noqa: E501
        :type cumulative_gas_used: str
        """
        if self.local_vars_configuration.client_side_validation and cumulative_gas_used is None:  # noqa: E501
            raise ValueError("Invalid value for `cumulative_gas_used`, must not be `None`")  # noqa: E501

        self._cumulative_gas_used = cumulative_gas_used

    @property
    def effective_gas_price(self):
        """Gets the effective_gas_price of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The effective_gas_price of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: str
        """
        return self._effective_gas_price

    @effective_gas_price.setter
    def effective_gas_price(self, effective_gas_price):
        """Sets the effective_gas_price of this SmartBchTransactionReceipt.


        :param effective_gas_price: The effective_gas_price of this SmartBchTransactionReceipt.  # noqa: E501
        :type effective_gas_price: str
        """
        if self.local_vars_configuration.client_side_validation and effective_gas_price is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_gas_price`, must not be `None`")  # noqa: E501

        self._effective_gas_price = effective_gas_price

    @property
    def byzantium(self):
        """Gets the byzantium of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The byzantium of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: bool
        """
        return self._byzantium

    @byzantium.setter
    def byzantium(self, byzantium):
        """Sets the byzantium of this SmartBchTransactionReceipt.


        :param byzantium: The byzantium of this SmartBchTransactionReceipt.  # noqa: E501
        :type byzantium: bool
        """
        if self.local_vars_configuration.client_side_validation and byzantium is None:  # noqa: E501
            raise ValueError("Invalid value for `byzantium`, must not be `None`")  # noqa: E501

        self._byzantium = byzantium

    @property
    def type(self):
        """Gets the type of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The type of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: float
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SmartBchTransactionReceipt.


        :param type: The type of this SmartBchTransactionReceipt.  # noqa: E501
        :type type: float
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this SmartBchTransactionReceipt.  # noqa: E501


        :return: The status of this SmartBchTransactionReceipt.  # noqa: E501
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SmartBchTransactionReceipt.


        :param status: The status of this SmartBchTransactionReceipt.  # noqa: E501
        :type status: float
        """

        self._status = status

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
        if not isinstance(other, SmartBchTransactionReceipt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchTransactionReceipt):
            return True

        return self.to_dict() != other.to_dict()
