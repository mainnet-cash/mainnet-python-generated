# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.5.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class GetAddressesResponse(object):
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
        'bchtest': 'str',
        'slptest': 'str',
        'sbchtest': 'str',
        'sbchcontract': 'str',
        'sbchtoken': 'str'
    }

    attribute_map = {
        'bchtest': 'bchtest',
        'slptest': 'slptest',
        'sbchtest': 'sbchtest',
        'sbchcontract': 'sbchcontract',
        'sbchtoken': 'sbchtoken'
    }

    def __init__(self, bchtest=None, slptest=None, sbchtest=None, sbchcontract=None, sbchtoken=None, local_vars_configuration=None):  # noqa: E501
        """GetAddressesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bchtest = None
        self._slptest = None
        self._sbchtest = None
        self._sbchcontract = None
        self._sbchtoken = None
        self.discriminator = None

        if bchtest is not None:
            self.bchtest = bchtest
        if slptest is not None:
            self.slptest = slptest
        if sbchtest is not None:
            self.sbchtest = sbchtest
        if sbchcontract is not None:
            self.sbchcontract = sbchcontract
        if sbchtoken is not None:
            self.sbchtoken = sbchtoken

    @property
    def bchtest(self):
        """Gets the bchtest of this GetAddressesResponse.  # noqa: E501

        Cashaddr to return testnet BCH  # noqa: E501

        :return: The bchtest of this GetAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._bchtest

    @bchtest.setter
    def bchtest(self, bchtest):
        """Sets the bchtest of this GetAddressesResponse.

        Cashaddr to return testnet BCH  # noqa: E501

        :param bchtest: The bchtest of this GetAddressesResponse.  # noqa: E501
        :type bchtest: str
        """

        self._bchtest = bchtest

    @property
    def slptest(self):
        """Gets the slptest of this GetAddressesResponse.  # noqa: E501

        Slpaddr to return testnet SLP tokens  # noqa: E501

        :return: The slptest of this GetAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._slptest

    @slptest.setter
    def slptest(self, slptest):
        """Sets the slptest of this GetAddressesResponse.

        Slpaddr to return testnet SLP tokens  # noqa: E501

        :param slptest: The slptest of this GetAddressesResponse.  # noqa: E501
        :type slptest: str
        """

        self._slptest = slptest

    @property
    def sbchtest(self):
        """Gets the sbchtest of this GetAddressesResponse.  # noqa: E501

        SmartBch testnet faucet contract owner address  # noqa: E501

        :return: The sbchtest of this GetAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._sbchtest

    @sbchtest.setter
    def sbchtest(self, sbchtest):
        """Sets the sbchtest of this GetAddressesResponse.

        SmartBch testnet faucet contract owner address  # noqa: E501

        :param sbchtest: The sbchtest of this GetAddressesResponse.  # noqa: E501
        :type sbchtest: str
        """

        self._sbchtest = sbchtest

    @property
    def sbchcontract(self):
        """Gets the sbchcontract of this GetAddressesResponse.  # noqa: E501

        SmartBch testnet contract address to return BCH and SEP20 tokens  # noqa: E501

        :return: The sbchcontract of this GetAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._sbchcontract

    @sbchcontract.setter
    def sbchcontract(self, sbchcontract):
        """Sets the sbchcontract of this GetAddressesResponse.

        SmartBch testnet contract address to return BCH and SEP20 tokens  # noqa: E501

        :param sbchcontract: The sbchcontract of this GetAddressesResponse.  # noqa: E501
        :type sbchcontract: str
        """

        self._sbchcontract = sbchcontract

    @property
    def sbchtoken(self):
        """Gets the sbchtoken of this GetAddressesResponse.  # noqa: E501

        SmartBch testnet sample SEP20 token address  # noqa: E501

        :return: The sbchtoken of this GetAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._sbchtoken

    @sbchtoken.setter
    def sbchtoken(self, sbchtoken):
        """Sets the sbchtoken of this GetAddressesResponse.

        SmartBch testnet sample SEP20 token address  # noqa: E501

        :param sbchtoken: The sbchtoken of this GetAddressesResponse.  # noqa: E501
        :type sbchtoken: str
        """

        self._sbchtoken = sbchtoken

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
        if not isinstance(other, GetAddressesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAddressesResponse):
            return True

        return self.to_dict() != other.to_dict()
