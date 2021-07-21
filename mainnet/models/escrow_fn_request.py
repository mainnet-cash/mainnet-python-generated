# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.32
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class EscrowFnRequest(object):
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
        'escrow_contract_id': 'str',
        'wallet_id': 'str',
        'function': 'str',
        'to': 'str',
        'action': 'str',
        'utxo_ids': 'list[str]'
    }

    attribute_map = {
        'escrow_contract_id': 'escrowContractId',
        'wallet_id': 'walletId',
        'function': 'function',
        'to': 'to',
        'action': 'action',
        'utxo_ids': 'utxoIds'
    }

    def __init__(self, escrow_contract_id=None, wallet_id=None, function=None, to=None, action=None, utxo_ids=None, local_vars_configuration=None):  # noqa: E501
        """EscrowFnRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._escrow_contract_id = None
        self._wallet_id = None
        self._function = None
        self._to = None
        self._action = None
        self._utxo_ids = None
        self.discriminator = None

        self.escrow_contract_id = escrow_contract_id
        self.wallet_id = wallet_id
        self.function = function
        if to is not None:
            self.to = to
        if action is not None:
            self.action = action
        if utxo_ids is not None:
            self.utxo_ids = utxo_ids

    @property
    def escrow_contract_id(self):
        """Gets the escrow_contract_id of this EscrowFnRequest.  # noqa: E501

        serialized contract   # noqa: E501

        :return: The escrow_contract_id of this EscrowFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._escrow_contract_id

    @escrow_contract_id.setter
    def escrow_contract_id(self, escrow_contract_id):
        """Sets the escrow_contract_id of this EscrowFnRequest.

        serialized contract   # noqa: E501

        :param escrow_contract_id: The escrow_contract_id of this EscrowFnRequest.  # noqa: E501
        :type escrow_contract_id: str
        """
        if self.local_vars_configuration.client_side_validation and escrow_contract_id is None:  # noqa: E501
            raise ValueError("Invalid value for `escrow_contract_id`, must not be `None`")  # noqa: E501

        self._escrow_contract_id = escrow_contract_id

    @property
    def wallet_id(self):
        """Gets the wallet_id of this EscrowFnRequest.  # noqa: E501

        The walletId of the transaction signer.   # noqa: E501

        :return: The wallet_id of this EscrowFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this EscrowFnRequest.

        The walletId of the transaction signer.   # noqa: E501

        :param wallet_id: The wallet_id of this EscrowFnRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def function(self):
        """Gets the function of this EscrowFnRequest.  # noqa: E501

        Function to call on the escrow contract.  # noqa: E501

        :return: The function of this EscrowFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this EscrowFnRequest.

        Function to call on the escrow contract.  # noqa: E501

        :param function: The function of this EscrowFnRequest.  # noqa: E501
        :type function: str
        """
        if self.local_vars_configuration.client_side_validation and function is None:  # noqa: E501
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501
        allowed_values = ["spend", "refund"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and function not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `function` ({0}), must be one of {1}"  # noqa: E501
                .format(function, allowed_values)
            )

        self._function = function

    @property
    def to(self):
        """Gets the to of this EscrowFnRequest.  # noqa: E501

        Output address for the transaction  # noqa: E501

        :return: The to of this EscrowFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EscrowFnRequest.

        Output address for the transaction  # noqa: E501

        :param to: The to of this EscrowFnRequest.  # noqa: E501
        :type to: str
        """

        self._to = to

    @property
    def action(self):
        """Gets the action of this EscrowFnRequest.  # noqa: E501

        In addition to `send`ing the built transaction, the built transaction hex may be returned (without broadcasting) with `build` action, or the [`meep 🔗`](https://github.com/gcash/meep) debugger command  # noqa: E501

        :return: The action of this EscrowFnRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EscrowFnRequest.

        In addition to `send`ing the built transaction, the built transaction hex may be returned (without broadcasting) with `build` action, or the [`meep 🔗`](https://github.com/gcash/meep) debugger command  # noqa: E501

        :param action: The action of this EscrowFnRequest.  # noqa: E501
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
    def utxo_ids(self):
        """Gets the utxo_ids of this EscrowFnRequest.  # noqa: E501


        :return: The utxo_ids of this EscrowFnRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._utxo_ids

    @utxo_ids.setter
    def utxo_ids(self, utxo_ids):
        """Sets the utxo_ids of this EscrowFnRequest.


        :param utxo_ids: The utxo_ids of this EscrowFnRequest.  # noqa: E501
        :type utxo_ids: list[str]
        """

        self._utxo_ids = utxo_ids

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
        if not isinstance(other, EscrowFnRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EscrowFnRequest):
            return True

        return self.to_dict() != other.to_dict()
