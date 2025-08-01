# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.7.14
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class ContractInfoResponse(object):
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
        'script': 'str',
        'parameters': 'list[str]',
        'cashaddr': 'str',
        'tokenaddr': 'str'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'script': 'script',
        'parameters': 'parameters',
        'cashaddr': 'cashaddr',
        'tokenaddr': 'tokenaddr'
    }

    def __init__(self, contract_id=None, script=None, parameters=None, cashaddr=None, tokenaddr=None, local_vars_configuration=None):  # noqa: E501
        """ContractInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contract_id = None
        self._script = None
        self._parameters = None
        self._cashaddr = None
        self._tokenaddr = None
        self.discriminator = None

        if contract_id is not None:
            self.contract_id = contract_id
        if script is not None:
            self.script = script
        if parameters is not None:
            self.parameters = parameters
        if cashaddr is not None:
            self.cashaddr = cashaddr
        if tokenaddr is not None:
            self.tokenaddr = tokenaddr

    @property
    def contract_id(self):
        """Gets the contract_id of this ContractInfoResponse.  # noqa: E501

        serialized contract   # noqa: E501

        :return: The contract_id of this ContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this ContractInfoResponse.

        serialized contract   # noqa: E501

        :param contract_id: The contract_id of this ContractInfoResponse.  # noqa: E501
        :type contract_id: str
        """

        self._contract_id = contract_id

    @property
    def script(self):
        """Gets the script of this ContractInfoResponse.  # noqa: E501

        The smart contract in cashscript syntax   # noqa: E501

        :return: The script of this ContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this ContractInfoResponse.

        The smart contract in cashscript syntax   # noqa: E501

        :param script: The script of this ContractInfoResponse.  # noqa: E501
        :type script: str
        """

        self._script = script

    @property
    def parameters(self):
        """Gets the parameters of this ContractInfoResponse.  # noqa: E501

        Parameters passed when the contract was created  # noqa: E501

        :return: The parameters of this ContractInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ContractInfoResponse.

        Parameters passed when the contract was created  # noqa: E501

        :param parameters: The parameters of this ContractInfoResponse.  # noqa: E501
        :type parameters: list[str]
        """

        self._parameters = parameters

    @property
    def cashaddr(self):
        """Gets the cashaddr of this ContractInfoResponse.  # noqa: E501


        :return: The cashaddr of this ContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this ContractInfoResponse.


        :param cashaddr: The cashaddr of this ContractInfoResponse.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def tokenaddr(self):
        """Gets the tokenaddr of this ContractInfoResponse.  # noqa: E501


        :return: The tokenaddr of this ContractInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._tokenaddr

    @tokenaddr.setter
    def tokenaddr(self, tokenaddr):
        """Sets the tokenaddr of this ContractInfoResponse.


        :param tokenaddr: The tokenaddr of this ContractInfoResponse.  # noqa: E501
        :type tokenaddr: str
        """

        self._tokenaddr = tokenaddr

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
        if not isinstance(other, ContractInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContractInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
