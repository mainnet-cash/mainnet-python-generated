# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.1.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SubmitTransactionRequest(object):
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
        'wallet_id': 'str',
        'transaction_hex': 'str',
        'await_propagation': 'bool'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'transaction_hex': 'transactionHex',
        'await_propagation': 'awaitPropagation'
    }

    def __init__(self, wallet_id=None, transaction_hex=None, await_propagation=True, local_vars_configuration=None):  # noqa: E501
        """SubmitTransactionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._transaction_hex = None
        self._await_propagation = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.transaction_hex = transaction_hex
        if await_propagation is not None:
            self.await_propagation = await_propagation

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SubmitTransactionRequest.  # noqa: E501


        :return: The wallet_id of this SubmitTransactionRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SubmitTransactionRequest.


        :param wallet_id: The wallet_id of this SubmitTransactionRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def transaction_hex(self):
        """Gets the transaction_hex of this SubmitTransactionRequest.  # noqa: E501

        encoded transaction in hex format  # noqa: E501

        :return: The transaction_hex of this SubmitTransactionRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hex

    @transaction_hex.setter
    def transaction_hex(self, transaction_hex):
        """Sets the transaction_hex of this SubmitTransactionRequest.

        encoded transaction in hex format  # noqa: E501

        :param transaction_hex: The transaction_hex of this SubmitTransactionRequest.  # noqa: E501
        :type transaction_hex: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_hex is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_hex`, must not be `None`")  # noqa: E501

        self._transaction_hex = transaction_hex

    @property
    def await_propagation(self):
        """Gets the await_propagation of this SubmitTransactionRequest.  # noqa: E501

        A boolean flag to wait for transaction to propagate through the network and be registered in the bitcoind and indexer. If set to false, the `send` call will be very fast, but the wallet UTXO state might be invalid for some 500ms.  # noqa: E501

        :return: The await_propagation of this SubmitTransactionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._await_propagation

    @await_propagation.setter
    def await_propagation(self, await_propagation):
        """Sets the await_propagation of this SubmitTransactionRequest.

        A boolean flag to wait for transaction to propagate through the network and be registered in the bitcoind and indexer. If set to false, the `send` call will be very fast, but the wallet UTXO state might be invalid for some 500ms.  # noqa: E501

        :param await_propagation: The await_propagation of this SubmitTransactionRequest.  # noqa: E501
        :type await_propagation: bool
        """

        self._await_propagation = await_propagation

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
        if not isinstance(other, SubmitTransactionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmitTransactionRequest):
            return True

        return self.to_dict() != other.to_dict()
