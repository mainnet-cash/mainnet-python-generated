# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.11
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractEstimateGasRequest(object):
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
        'contract_id': 'str',
        'function': 'str',
        'arguments': 'list[object]',
        'overrides': 'SmartBchOverrides'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'contract_id': 'contractId',
        'function': 'function',
        'arguments': 'arguments',
        'overrides': 'overrides'
    }

    def __init__(self, wallet_id=None, contract_id=None, function=None, arguments=None, overrides=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractEstimateGasRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._contract_id = None
        self._function = None
        self._arguments = None
        self._overrides = None
        self.discriminator = None

        if wallet_id is not None:
            self.wallet_id = wallet_id
        self.contract_id = contract_id
        self.function = function
        if arguments is not None:
            self.arguments = arguments
        if overrides is not None:
            self.overrides = overrides

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SmartBchContractEstimateGasRequest.  # noqa: E501

        Serialized wallet  # noqa: E501

        :return: The wallet_id of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SmartBchContractEstimateGasRequest.

        Serialized wallet  # noqa: E501

        :param wallet_id: The wallet_id of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :type wallet_id: str
        """

        self._wallet_id = wallet_id

    @property
    def contract_id(self):
        """Gets the contract_id of this SmartBchContractEstimateGasRequest.  # noqa: E501

        serialized contract  # noqa: E501

        :return: The contract_id of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this SmartBchContractEstimateGasRequest.

        serialized contract  # noqa: E501

        :param contract_id: The contract_id of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :type contract_id: str
        """
        if self.local_vars_configuration.client_side_validation and contract_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def function(self):
        """Gets the function of this SmartBchContractEstimateGasRequest.  # noqa: E501

        Function to call on the SmartBch contract.  # noqa: E501

        :return: The function of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this SmartBchContractEstimateGasRequest.

        Function to call on the SmartBch contract.  # noqa: E501

        :param function: The function of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :type function: str
        """
        if self.local_vars_configuration.client_side_validation and function is None:  # noqa: E501
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501

        self._function = function

    @property
    def arguments(self):
        """Gets the arguments of this SmartBchContractEstimateGasRequest.  # noqa: E501

        Arguments for the contract function call. Binary and BigNumber data should be passed as hexadecimal.   # noqa: E501

        :return: The arguments of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this SmartBchContractEstimateGasRequest.

        Arguments for the contract function call. Binary and BigNumber data should be passed as hexadecimal.   # noqa: E501

        :param arguments: The arguments of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :type arguments: list[object]
        """

        self._arguments = arguments

    @property
    def overrides(self):
        """Gets the overrides of this SmartBchContractEstimateGasRequest.  # noqa: E501


        :return: The overrides of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :rtype: SmartBchOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this SmartBchContractEstimateGasRequest.


        :param overrides: The overrides of this SmartBchContractEstimateGasRequest.  # noqa: E501
        :type overrides: SmartBchOverrides
        """

        self._overrides = overrides

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
        if not isinstance(other, SmartBchContractEstimateGasRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractEstimateGasRequest):
            return True

        return self.to_dict() != other.to_dict()
