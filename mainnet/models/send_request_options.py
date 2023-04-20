# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.4
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SendRequestOptions(object):
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
        'utxo_ids': 'list[str]',
        'change_address': 'str',
        'slp_aware': 'bool',
        'slp_semi_aware': 'bool',
        'query_balance': 'bool',
        'await_transaction_propagation': 'bool',
        'fee_paid_by': 'str',
        'check_token_quantities': 'bool'
    }

    attribute_map = {
        'utxo_ids': 'utxoIds',
        'change_address': 'changeAddress',
        'slp_aware': 'slpAware',
        'slp_semi_aware': 'slpSemiAware',
        'query_balance': 'queryBalance',
        'await_transaction_propagation': 'awaitTransactionPropagation',
        'fee_paid_by': 'feePaidBy',
        'check_token_quantities': 'checkTokenQuantities'
    }

    def __init__(self, utxo_ids=None, change_address=None, slp_aware=False, slp_semi_aware=False, query_balance=True, await_transaction_propagation=True, fee_paid_by='change', check_token_quantities=True, local_vars_configuration=None):  # noqa: E501
        """SendRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._utxo_ids = None
        self._change_address = None
        self._slp_aware = None
        self._slp_semi_aware = None
        self._query_balance = None
        self._await_transaction_propagation = None
        self._fee_paid_by = None
        self._check_token_quantities = None
        self.discriminator = None

        if utxo_ids is not None:
            self.utxo_ids = utxo_ids
        if change_address is not None:
            self.change_address = change_address
        if slp_aware is not None:
            self.slp_aware = slp_aware
        if slp_semi_aware is not None:
            self.slp_semi_aware = slp_semi_aware
        if query_balance is not None:
            self.query_balance = query_balance
        if await_transaction_propagation is not None:
            self.await_transaction_propagation = await_transaction_propagation
        if fee_paid_by is not None:
            self.fee_paid_by = fee_paid_by
        if check_token_quantities is not None:
            self.check_token_quantities = check_token_quantities

    @property
    def utxo_ids(self):
        """Gets the utxo_ids of this SendRequestOptions.  # noqa: E501


        :return: The utxo_ids of this SendRequestOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._utxo_ids

    @utxo_ids.setter
    def utxo_ids(self, utxo_ids):
        """Sets the utxo_ids of this SendRequestOptions.


        :param utxo_ids: The utxo_ids of this SendRequestOptions.  # noqa: E501
        :type utxo_ids: list[str]
        """

        self._utxo_ids = utxo_ids

    @property
    def change_address(self):
        """Gets the change_address of this SendRequestOptions.  # noqa: E501

        Cash address to receive change to   # noqa: E501

        :return: The change_address of this SendRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._change_address

    @change_address.setter
    def change_address(self, change_address):
        """Sets the change_address of this SendRequestOptions.

        Cash address to receive change to   # noqa: E501

        :param change_address: The change_address of this SendRequestOptions.  # noqa: E501
        :type change_address: str
        """

        self._change_address = change_address

    @property
    def slp_aware(self):
        """Gets the slp_aware of this SendRequestOptions.  # noqa: E501

        If you have any SLP tokens on the address, you should set `slpAware` to `true` to prevent accidental token burning This flag activates utxo checking against an external slp indexer So far this option is not switched on by default  # noqa: E501

        :return: The slp_aware of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._slp_aware

    @slp_aware.setter
    def slp_aware(self, slp_aware):
        """Sets the slp_aware of this SendRequestOptions.

        If you have any SLP tokens on the address, you should set `slpAware` to `true` to prevent accidental token burning This flag activates utxo checking against an external slp indexer So far this option is not switched on by default  # noqa: E501

        :param slp_aware: The slp_aware of this SendRequestOptions.  # noqa: E501
        :type slp_aware: bool
        """

        self._slp_aware = slp_aware

    @property
    def slp_semi_aware(self):
        """Gets the slp_semi_aware of this SendRequestOptions.  # noqa: E501

        This flag requires an utxo to have more than 546 sats to be spendable and counted in the balance This option is not switched on by default  # noqa: E501

        :return: The slp_semi_aware of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._slp_semi_aware

    @slp_semi_aware.setter
    def slp_semi_aware(self, slp_semi_aware):
        """Sets the slp_semi_aware of this SendRequestOptions.

        This flag requires an utxo to have more than 546 sats to be spendable and counted in the balance This option is not switched on by default  # noqa: E501

        :param slp_semi_aware: The slp_semi_aware of this SendRequestOptions.  # noqa: E501
        :type slp_semi_aware: bool
        """

        self._slp_semi_aware = slp_semi_aware

    @property
    def query_balance(self):
        """Gets the query_balance of this SendRequestOptions.  # noqa: E501

        A boolean flag to include the wallet balance after the successful `send` operation to the returned result If set to false, the balance will not be queried and returned, making the `send` call faster  # noqa: E501

        :return: The query_balance of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._query_balance

    @query_balance.setter
    def query_balance(self, query_balance):
        """Sets the query_balance of this SendRequestOptions.

        A boolean flag to include the wallet balance after the successful `send` operation to the returned result If set to false, the balance will not be queried and returned, making the `send` call faster  # noqa: E501

        :param query_balance: The query_balance of this SendRequestOptions.  # noqa: E501
        :type query_balance: bool
        """

        self._query_balance = query_balance

    @property
    def await_transaction_propagation(self):
        """Gets the await_transaction_propagation of this SendRequestOptions.  # noqa: E501

        A boolean flag to wait for transaction to propagate through the network and be registered in the bitcoind and indexer. If set to false, the `send` call will be very fast, but the wallet UTXO state might be invalid for some 500ms.  # noqa: E501

        :return: The await_transaction_propagation of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._await_transaction_propagation

    @await_transaction_propagation.setter
    def await_transaction_propagation(self, await_transaction_propagation):
        """Sets the await_transaction_propagation of this SendRequestOptions.

        A boolean flag to wait for transaction to propagate through the network and be registered in the bitcoind and indexer. If set to false, the `send` call will be very fast, but the wallet UTXO state might be invalid for some 500ms.  # noqa: E501

        :param await_transaction_propagation: The await_transaction_propagation of this SendRequestOptions.  # noqa: E501
        :type await_transaction_propagation: bool
        """

        self._await_transaction_propagation = await_transaction_propagation

    @property
    def fee_paid_by(self):
        """Gets the fee_paid_by of this SendRequestOptions.  # noqa: E501

        Fee allocation stragety. Convenience option to subtract fees from outputs if change is not sufficent to cover transaction costs.   * `change` - Change, pay the fees from change or error   * `firstOutput` - First Output, pay the fee from the first output or error   * `lastOutput` - Last Output, pay the fee from the last output or error   * `anyOutput` - Any Output, pay the fee from dust outputs or divide across all remaining non-dust outputs.   * `changeThenFirst` - Use change then first output or error.   * `changeThenLast` - Use change then last output or error.   * `changeThenAny` - Use change then any output stragety or error.   # noqa: E501

        :return: The fee_paid_by of this SendRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._fee_paid_by

    @fee_paid_by.setter
    def fee_paid_by(self, fee_paid_by):
        """Sets the fee_paid_by of this SendRequestOptions.

        Fee allocation stragety. Convenience option to subtract fees from outputs if change is not sufficent to cover transaction costs.   * `change` - Change, pay the fees from change or error   * `firstOutput` - First Output, pay the fee from the first output or error   * `lastOutput` - Last Output, pay the fee from the last output or error   * `anyOutput` - Any Output, pay the fee from dust outputs or divide across all remaining non-dust outputs.   * `changeThenFirst` - Use change then first output or error.   * `changeThenLast` - Use change then last output or error.   * `changeThenAny` - Use change then any output stragety or error.   # noqa: E501

        :param fee_paid_by: The fee_paid_by of this SendRequestOptions.  # noqa: E501
        :type fee_paid_by: str
        """
        allowed_values = ["change", "firstOutput", "anyOutputs", "lastOutput", "changeThenFirst", "changeThenAny", "changeThenLast"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fee_paid_by not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fee_paid_by` ({0}), must be one of {1}"  # noqa: E501
                .format(fee_paid_by, allowed_values)
            )

        self._fee_paid_by = fee_paid_by

    @property
    def check_token_quantities(self):
        """Gets the check_token_quantities of this SendRequestOptions.  # noqa: E501

        Check that sum of input amounts and output amount for each token category matches. Prevents accidental burns.   # noqa: E501

        :return: The check_token_quantities of this SendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._check_token_quantities

    @check_token_quantities.setter
    def check_token_quantities(self, check_token_quantities):
        """Sets the check_token_quantities of this SendRequestOptions.

        Check that sum of input amounts and output amount for each token category matches. Prevents accidental burns.   # noqa: E501

        :param check_token_quantities: The check_token_quantities of this SendRequestOptions.  # noqa: E501
        :type check_token_quantities: bool
        """

        self._check_token_quantities = check_token_quantities

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
        if not isinstance(other, SendRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
