# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.23
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class SmartBchContractDeployRequest(object):
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
        'script': 'str',
        'parameters': 'list[object]',
        'overrides': 'SmartBchOverrides'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'script': 'script',
        'parameters': 'parameters',
        'overrides': 'overrides'
    }

    def __init__(self, wallet_id=None, script=None, parameters=None, overrides=None, local_vars_configuration=None):  # noqa: E501
        """SmartBchContractDeployRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._script = None
        self._parameters = None
        self._overrides = None
        self.discriminator = None

        self.wallet_id = wallet_id
        self.script = script
        if parameters is not None:
            self.parameters = parameters
        if overrides is not None:
            self.overrides = overrides

    @property
    def wallet_id(self):
        """Gets the wallet_id of this SmartBchContractDeployRequest.  # noqa: E501

        Serialized wallet  # noqa: E501

        :return: The wallet_id of this SmartBchContractDeployRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this SmartBchContractDeployRequest.

        Serialized wallet  # noqa: E501

        :param wallet_id: The wallet_id of this SmartBchContractDeployRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def script(self):
        """Gets the script of this SmartBchContractDeployRequest.  # noqa: E501

        solidity source code used to create this contract instance  # noqa: E501

        :return: The script of this SmartBchContractDeployRequest.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this SmartBchContractDeployRequest.

        solidity source code used to create this contract instance  # noqa: E501

        :param script: The script of this SmartBchContractDeployRequest.  # noqa: E501
        :type script: str
        """
        if self.local_vars_configuration.client_side_validation and script is None:  # noqa: E501
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

    @property
    def parameters(self):
        """Gets the parameters of this SmartBchContractDeployRequest.  # noqa: E501

        constructor parameters used to create this contract instance  # noqa: E501

        :return: The parameters of this SmartBchContractDeployRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SmartBchContractDeployRequest.

        constructor parameters used to create this contract instance  # noqa: E501

        :param parameters: The parameters of this SmartBchContractDeployRequest.  # noqa: E501
        :type parameters: list[object]
        """

        self._parameters = parameters

    @property
    def overrides(self):
        """Gets the overrides of this SmartBchContractDeployRequest.  # noqa: E501


        :return: The overrides of this SmartBchContractDeployRequest.  # noqa: E501
        :rtype: SmartBchOverrides
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this SmartBchContractDeployRequest.


        :param overrides: The overrides of this SmartBchContractDeployRequest.  # noqa: E501
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
        if not isinstance(other, SmartBchContractDeployRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartBchContractDeployRequest):
            return True

        return self.to_dict() != other.to_dict()
