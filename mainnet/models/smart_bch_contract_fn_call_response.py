# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.14
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractFnCallResponse(object):
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
        'result': 'object',
        'tx_id': 'str',
        'receipt': 'SmartBchTransactionReceipt'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'result': 'result',
        'tx_id': 'txId',
        'receipt': 'receipt'
    }

    def __init__(self, contract_id=None, result=None, tx_id=None, receipt=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractFnCallResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract_id = None
        self._result = None
        self._tx_id = None
        self._receipt = None
        self.discriminator = None

        if contract_id is not None:
            self.contract_id = contract_id
        self.result = result
        if tx_id is not None:
            self.tx_id = tx_id
        if receipt is not None:
            self.receipt = receipt

    @property
    def contract_id(self):
        """Gets the contract_id of this SmartBchContractFnCallResponse.  # noqa: E501

        serialized contract  # noqa: E501

        :return: The contract_id of this SmartBchContractFnCallResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this SmartBchContractFnCallResponse.

        serialized contract  # noqa: E501

        :param contract_id: The contract_id of this SmartBchContractFnCallResponse.  # noqa: E501
        :type contract_id: str
        """

        self._contract_id = contract_id

    @property
    def result(self):
        """Gets the result of this SmartBchContractFnCallResponse.  # noqa: E501

        contract function evaluation result. Can be of any type.  # noqa: E501

        :return: The result of this SmartBchContractFnCallResponse.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SmartBchContractFnCallResponse.

        contract function evaluation result. Can be of any type.  # noqa: E501

        :param result: The result of this SmartBchContractFnCallResponse.  # noqa: E501
        :type result: object
        """

        self._result = result

    @property
    def tx_id(self):
        """Gets the tx_id of this SmartBchContractFnCallResponse.  # noqa: E501

        The hash of a transaction  # noqa: E501

        :return: The tx_id of this SmartBchContractFnCallResponse.  # noqa: E501
        :rtype: str
        """
        return self._tx_id

    @tx_id.setter
    def tx_id(self, tx_id):
        """Sets the tx_id of this SmartBchContractFnCallResponse.

        The hash of a transaction  # noqa: E501

        :param tx_id: The tx_id of this SmartBchContractFnCallResponse.  # noqa: E501
        :type tx_id: str
        """

        self._tx_id = tx_id

    @property
    def receipt(self):
        """Gets the receipt of this SmartBchContractFnCallResponse.  # noqa: E501


        :return: The receipt of this SmartBchContractFnCallResponse.  # noqa: E501
        :rtype: SmartBchTransactionReceipt
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """Sets the receipt of this SmartBchContractFnCallResponse.


        :param receipt: The receipt of this SmartBchContractFnCallResponse.  # noqa: E501
        :type receipt: SmartBchTransactionReceipt
        """

        self._receipt = receipt

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
        if not isinstance(other, SmartBchContractFnCallResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractFnCallResponse):
            return True

        return self.to_dict() != other.to_dict()
