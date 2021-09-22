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


class SmartBchContractInfoResponse(object):
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
        'address': 'str',
        'abi': 'list[str]',
        'script': 'str',
        'parameters': 'list[object]'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'address': 'address',
        'abi': 'abi',
        'script': 'script',
        'parameters': 'parameters'
    }

    def __init__(self, contract_id=None, address=None, abi=None, script=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract_id = None
        self._address = None
        self._abi = None
        self._script = None
        self._parameters = None
        self.discriminator = None

        if contract_id is not None:
            self.contract_id = contract_id
        if address is not None:
            self.address = address
        if abi is not None:
            self.abi = abi
        if script is not None:
            self.script = script
        if parameters is not None:
            self.parameters = parameters

    @property
    def contract_id(self):
        """Gets the contract_id of this SmartBchContractInfoResponse.  # noqa: E501

        serialized contract  # noqa: E501

        :return: The contract_id of this SmartBchContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this SmartBchContractInfoResponse.

        serialized contract  # noqa: E501

        :param contract_id: The contract_id of this SmartBchContractInfoResponse.  # noqa: E501
        :type contract_id: str
        """

        self._contract_id = contract_id

    @property
    def address(self):
        """Gets the address of this SmartBchContractInfoResponse.  # noqa: E501

        Address of an already deployed contract  # noqa: E501

        :return: The address of this SmartBchContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SmartBchContractInfoResponse.

        Address of an already deployed contract  # noqa: E501

        :param address: The address of this SmartBchContractInfoResponse.  # noqa: E501
        :type address: str
        """

        self._address = address

    @property
    def abi(self):
        """Gets the abi of this SmartBchContractInfoResponse.  # noqa: E501

        Contract ABI (Application Binary Interface), which describes the contract interaction  # noqa: E501

        :return: The abi of this SmartBchContractInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._abi

    @abi.setter
    def abi(self, abi):
        """Sets the abi of this SmartBchContractInfoResponse.

        Contract ABI (Application Binary Interface), which describes the contract interaction  # noqa: E501

        :param abi: The abi of this SmartBchContractInfoResponse.  # noqa: E501
        :type abi: list[str]
        """

        self._abi = abi

    @property
    def script(self):
        """Gets the script of this SmartBchContractInfoResponse.  # noqa: E501

        solidity source code used to create this contract instance  # noqa: E501

        :return: The script of this SmartBchContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this SmartBchContractInfoResponse.

        solidity source code used to create this contract instance  # noqa: E501

        :param script: The script of this SmartBchContractInfoResponse.  # noqa: E501
        :type script: str
        """

        self._script = script

    @property
    def parameters(self):
        """Gets the parameters of this SmartBchContractInfoResponse.  # noqa: E501

        constructor parameters used to create this contract instance  # noqa: E501

        :return: The parameters of this SmartBchContractInfoResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SmartBchContractInfoResponse.

        constructor parameters used to create this contract instance  # noqa: E501

        :param parameters: The parameters of this SmartBchContractInfoResponse.  # noqa: E501
        :type parameters: list[object]
        """

        self._parameters = parameters

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
        if not isinstance(other, SmartBchContractInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
