# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.10
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchSendRequestOptions(object):
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
        'query_balance': 'bool',
        'await_transaction_propagation': 'bool'
    }

    attribute_map = {
        'query_balance': 'queryBalance',
        'await_transaction_propagation': 'awaitTransactionPropagation'
    }

    def __init__(self, query_balance=True, await_transaction_propagation=True, local_vars_configuration=None):  # noqa: E501
        """SmartBchSendRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._query_balance = None
        self._await_transaction_propagation = None
        self.discriminator = None

        if query_balance is not None:
            self.query_balance = query_balance
        if await_transaction_propagation is not None:
            self.await_transaction_propagation = await_transaction_propagation

    @property
    def query_balance(self):
        """Gets the query_balance of this SmartBchSendRequestOptions.  # noqa: E501

        A boolean flag to include the wallet balance after the successful `send` operation to the returned result If set to false, the balance will not be queried and returned, making the `send` call faster  # noqa: E501

        :return: The query_balance of this SmartBchSendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._query_balance

    @query_balance.setter
    def query_balance(self, query_balance):
        """Sets the query_balance of this SmartBchSendRequestOptions.

        A boolean flag to include the wallet balance after the successful `send` operation to the returned result If set to false, the balance will not be queried and returned, making the `send` call faster  # noqa: E501

        :param query_balance: The query_balance of this SmartBchSendRequestOptions.  # noqa: E501
        :type query_balance: bool
        """

        self._query_balance = query_balance

    @property
    def await_transaction_propagation(self):
        """Gets the await_transaction_propagation of this SmartBchSendRequestOptions.  # noqa: E501

        A boolean flag to wait for transaction to propagate through the network. If set to false, the `send` call will be faster, but other subsequent operations might fail due to nonce number mismatch.  # noqa: E501

        :return: The await_transaction_propagation of this SmartBchSendRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._await_transaction_propagation

    @await_transaction_propagation.setter
    def await_transaction_propagation(self, await_transaction_propagation):
        """Sets the await_transaction_propagation of this SmartBchSendRequestOptions.

        A boolean flag to wait for transaction to propagate through the network. If set to false, the `send` call will be faster, but other subsequent operations might fail due to nonce number mismatch.  # noqa: E501

        :param await_transaction_propagation: The await_transaction_propagation of this SmartBchSendRequestOptions.  # noqa: E501
        :type await_transaction_propagation: bool
        """

        self._await_transaction_propagation = await_transaction_propagation

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
        if not isinstance(other, SmartBchSendRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchSendRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
