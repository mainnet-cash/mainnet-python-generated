# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.31
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ContractFnRequest(object):
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
        'contract_id': 'str',
        'action': 'str',
        'function': 'str',
        'arguments': 'list[str]',
        'to': 'AnyOfSendRequestItemarrayCashscriptReceiptarray',
        'utxo_ids': 'list[str]',
        'op_return': 'list[str]',
        'fee_per_byte': 'float',
        'hardcoded_fee': 'float',
        'min_change': 'float',
        'without_change': 'bool',
        'age': 'float',
        'time': 'float'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'action': 'action',
        'function': 'function',
        'arguments': 'arguments',
        'to': 'to',
        'utxo_ids': 'utxoIds',
        'op_return': 'opReturn',
        'fee_per_byte': 'feePerByte',
        'hardcoded_fee': 'hardcodedFee',
        'min_change': 'minChange',
        'without_change': 'withoutChange',
        'age': 'age',
        'time': 'time'
    }

    def __init__(self, contract_id=None, action='send', function=None, arguments=None, to=None, utxo_ids=None, op_return=None, fee_per_byte=None, hardcoded_fee=None, min_change=None, without_change=False, age=None, time=None, local_vars_configuration=None):  # noqa: E501
        """ContractFnRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract_id = None
        self._action = None
        self._function = None
        self._arguments = None
        self._to = None
        self._utxo_ids = None
        self._op_return = None
        self._fee_per_byte = None
        self._hardcoded_fee = None
        self._min_change = None
        self._without_change = None
        self._age = None
        self._time = None
        self.discriminator = None

        self.contract_id = contract_id
        if action is not None:
            self.action = action
        self.function = function
        if arguments is not None:
            self.arguments = arguments
        self.to = to
        if utxo_ids is not None:
            self.utxo_ids = utxo_ids
        if op_return is not None:
            self.op_return = op_return
        if fee_per_byte is not None:
            self.fee_per_byte = fee_per_byte
        if hardcoded_fee is not None:
            self.hardcoded_fee = hardcoded_fee
        if min_change is not None:
            self.min_change = min_change
        if without_change is not None:
            self.without_change = without_change
        if age is not None:
            self.age = age
        if time is not None:
            self.time = time

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractFnRequest.  # noqa: E501

        serialized contract   # noqa: E501

        :return: The contract_id of this ContractFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractFnRequest.

        serialized contract   # noqa: E501

        :param contract_id: The contract_id of this ContractFnRequest.  # noqa: E501
        :type contract_id: str
        """
        if self.local_vars_configuration.client_side_validation and contract_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def action(self):
        """Gets the action of this ContractFnRequest.  # noqa: E501

        In addition to `send`ing the built transaction, the built transaction hex may be returned (without broadcasting) with `build` action, or the [`meep 🔗`](https://github.com/gcash/meep) debugger command.  # noqa: E501

        :return: The action of this ContractFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ContractFnRequest.

        In addition to `send`ing the built transaction, the built transaction hex may be returned (without broadcasting) with `build` action, or the [`meep 🔗`](https://github.com/gcash/meep) debugger command.  # noqa: E501

        :param action: The action of this ContractFnRequest.  # noqa: E501
        :type action: str
        """
        allowed_values = ["build", "send", "meep"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def function(self):
        """Gets the function of this ContractFnRequest.  # noqa: E501

        Function to call on the cashscript contract.  # noqa: E501

        :return: The function of this ContractFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this ContractFnRequest.

        Function to call on the cashscript contract.  # noqa: E501

        :param function: The function of this ContractFnRequest.  # noqa: E501
        :type function: str
        """
        if self.local_vars_configuration.client_side_validation and function is None:  # noqa: E501
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501

        self._function = function

    @property
    def arguments(self):
        """Gets the arguments of this ContractFnRequest.  # noqa: E501

        Arguments for the contract function call as strings.  Binary data should be passed as hexidecimal.  Signatures may be passed as wallet import format (WIF) or wallet strings (walletId). Cashscript expects `pubkey`s to be compressed 35 byte values.   # noqa: E501

        :return: The arguments of this ContractFnRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ContractFnRequest.

        Arguments for the contract function call as strings.  Binary data should be passed as hexidecimal.  Signatures may be passed as wallet import format (WIF) or wallet strings (walletId). Cashscript expects `pubkey`s to be compressed 35 byte values.   # noqa: E501

        :param arguments: The arguments of this ContractFnRequest.  # noqa: E501
        :type arguments: list[str]
        """

        self._arguments = arguments

    @property
    def to(self):
        """Gets the to of this ContractFnRequest.  # noqa: E501

        The output destination, as a SendRequest, cashscript style output(s), array of either.  # noqa: E501

        :return: The to of this ContractFnRequest.  # noqa: E501
        :rtype: AnyOfSendRequestItemarrayCashscriptReceiptarray
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ContractFnRequest.

        The output destination, as a SendRequest, cashscript style output(s), array of either.  # noqa: E501

        :param to: The to of this ContractFnRequest.  # noqa: E501
        :type to: AnyOfSendRequestItemarrayCashscriptReceiptarray
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def utxo_ids(self):
        """Gets the utxo_ids of this ContractFnRequest.  # noqa: E501

        Serialized utxoId(s) to spend from  # noqa: E501

        :return: The utxo_ids of this ContractFnRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._utxo_ids

    @utxo_ids.setter
    def utxo_ids(self, utxo_ids):
        """Sets the utxo_ids of this ContractFnRequest.

        Serialized utxoId(s) to spend from  # noqa: E501

        :param utxo_ids: The utxo_ids of this ContractFnRequest.  # noqa: E501
        :type utxo_ids: list[str]
        """

        self._utxo_ids = utxo_ids

    @property
    def op_return(self):
        """Gets the op_return of this ContractFnRequest.  # noqa: E501

        Add OP_RETURN outputs to the transaction. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withopreturn)   # noqa: E501

        :return: The op_return of this ContractFnRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._op_return

    @op_return.setter
    def op_return(self, op_return):
        """Sets the op_return of this ContractFnRequest.

        Add OP_RETURN outputs to the transaction. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withopreturn)   # noqa: E501

        :param op_return: The op_return of this ContractFnRequest.  # noqa: E501
        :type op_return: list[str]
        """

        self._op_return = op_return

    @property
    def fee_per_byte(self):
        """Gets the fee_per_byte of this ContractFnRequest.  # noqa: E501

        The withFeePerByte() function allows you to specify the fee per per bytes for the transaction. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withfeeperbyte)   # noqa: E501

        :return: The fee_per_byte of this ContractFnRequest.  # noqa: E501
        :rtype: float
        """
        return self._fee_per_byte

    @fee_per_byte.setter
    def fee_per_byte(self, fee_per_byte):
        """Sets the fee_per_byte of this ContractFnRequest.

        The withFeePerByte() function allows you to specify the fee per per bytes for the transaction. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withfeeperbyte)   # noqa: E501

        :param fee_per_byte: The fee_per_byte of this ContractFnRequest.  # noqa: E501
        :type fee_per_byte: float
        """

        self._fee_per_byte = fee_per_byte

    @property
    def hardcoded_fee(self):
        """Gets the hardcoded_fee of this ContractFnRequest.  # noqa: E501

        Specify a hardcoded fee to the transaction. By default the transaction fee is automatically calculated by the CashScript SDK. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withhardcodedfee)   # noqa: E501

        :return: The hardcoded_fee of this ContractFnRequest.  # noqa: E501
        :rtype: float
        """
        return self._hardcoded_fee

    @hardcoded_fee.setter
    def hardcoded_fee(self, hardcoded_fee):
        """Sets the hardcoded_fee of this ContractFnRequest.

        Specify a hardcoded fee to the transaction. By default the transaction fee is automatically calculated by the CashScript SDK. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withhardcodedfee)   # noqa: E501

        :param hardcoded_fee: The hardcoded_fee of this ContractFnRequest.  # noqa: E501
        :type hardcoded_fee: float
        """

        self._hardcoded_fee = hardcoded_fee

    @property
    def min_change(self):
        """Gets the min_change of this ContractFnRequest.  # noqa: E501

        Set a threshold for including a change output. Any remaining amount under this threshold will be added to the transaction fee instead. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withminchange)   # noqa: E501

        :return: The min_change of this ContractFnRequest.  # noqa: E501
        :rtype: float
        """
        return self._min_change

    @min_change.setter
    def min_change(self, min_change):
        """Sets the min_change of this ContractFnRequest.

        Set a threshold for including a change output. Any remaining amount under this threshold will be added to the transaction fee instead. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withminchange)   # noqa: E501

        :param min_change: The min_change of this ContractFnRequest.  # noqa: E501
        :type min_change: float
        """

        self._min_change = min_change

    @property
    def without_change(self):
        """Gets the without_change of this ContractFnRequest.  # noqa: E501

        Disable the change output. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withoutchange)   # noqa: E501

        :return: The without_change of this ContractFnRequest.  # noqa: E501
        :rtype: bool
        """
        return self._without_change

    @without_change.setter
    def without_change(self, without_change):
        """Sets the without_change of this ContractFnRequest.

        Disable the change output. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withoutchange)   # noqa: E501

        :param without_change: The without_change of this ContractFnRequest.  # noqa: E501
        :type without_change: bool
        """

        self._without_change = without_change

    @property
    def age(self):
        """Gets the age of this ContractFnRequest.  # noqa: E501

        Specify the minimum age of the transaction inputs. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withage)   # noqa: E501

        :return: The age of this ContractFnRequest.  # noqa: E501
        :rtype: float
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this ContractFnRequest.

        Specify the minimum age of the transaction inputs. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withage)   # noqa: E501

        :param age: The age of this ContractFnRequest.  # noqa: E501
        :type age: float
        """

        self._age = age

    @property
    def time(self):
        """Gets the time of this ContractFnRequest.  # noqa: E501

        Specify the minimum block number that the transaction can be included in. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withtime)   # noqa: E501

        :return: The time of this ContractFnRequest.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ContractFnRequest.

        Specify the minimum block number that the transaction can be included in. See [cashscript docs](https://cashscript.org/docs/sdk/transactions#withtime)   # noqa: E501

        :param time: The time of this ContractFnRequest.  # noqa: E501
        :type time: float
        """

        self._time = time

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
        if not isinstance(other, ContractFnRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContractFnRequest):
            return True

        return self.to_dict() != other.to_dict()
