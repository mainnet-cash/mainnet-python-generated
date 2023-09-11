# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 1.1.34-alpha.0
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class EscrowRequest(object):
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
        'buyer_addr': 'object',
        'arbiter_addr': 'object',
        'seller_addr': 'object',
        'amount': 'float'
    }

    attribute_map = {
        'buyer_addr': 'buyerAddr',
        'arbiter_addr': 'arbiterAddr',
        'seller_addr': 'sellerAddr',
        'amount': 'amount'
    }

    def __init__(self, buyer_addr=None, arbiter_addr=None, seller_addr=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """EscrowRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._buyer_addr = None
        self._arbiter_addr = None
        self._seller_addr = None
        self._amount = None
        self.discriminator = None

        self.buyer_addr = buyer_addr
        self.arbiter_addr = arbiter_addr
        self.seller_addr = seller_addr
        self.amount = amount

    @property
    def buyer_addr(self):
        """Gets the buyer_addr of this EscrowRequest.  # noqa: E501

        The cashaddress of the buyer  # noqa: E501

        :return: The buyer_addr of this EscrowRequest.  # noqa: E501
        :rtype: object
        """
        return self._buyer_addr

    @buyer_addr.setter
    def buyer_addr(self, buyer_addr):
        """Sets the buyer_addr of this EscrowRequest.

        The cashaddress of the buyer  # noqa: E501

        :param buyer_addr: The buyer_addr of this EscrowRequest.  # noqa: E501
        :type buyer_addr: object
        """

        self._buyer_addr = buyer_addr

    @property
    def arbiter_addr(self):
        """Gets the arbiter_addr of this EscrowRequest.  # noqa: E501

        The cashaddress of the arbiter  # noqa: E501

        :return: The arbiter_addr of this EscrowRequest.  # noqa: E501
        :rtype: object
        """
        return self._arbiter_addr

    @arbiter_addr.setter
    def arbiter_addr(self, arbiter_addr):
        """Sets the arbiter_addr of this EscrowRequest.

        The cashaddress of the arbiter  # noqa: E501

        :param arbiter_addr: The arbiter_addr of this EscrowRequest.  # noqa: E501
        :type arbiter_addr: object
        """

        self._arbiter_addr = arbiter_addr

    @property
    def seller_addr(self):
        """Gets the seller_addr of this EscrowRequest.  # noqa: E501

        The cashaddress of the seller  # noqa: E501

        :return: The seller_addr of this EscrowRequest.  # noqa: E501
        :rtype: object
        """
        return self._seller_addr

    @seller_addr.setter
    def seller_addr(self, seller_addr):
        """Sets the seller_addr of this EscrowRequest.

        The cashaddress of the seller  # noqa: E501

        :param seller_addr: The seller_addr of this EscrowRequest.  # noqa: E501
        :type seller_addr: object
        """

        self._seller_addr = seller_addr

    @property
    def amount(self):
        """Gets the amount of this EscrowRequest.  # noqa: E501

        Numeric amount to be transferred by the contract in satoshi, amount must be less than 21 BCH.  # noqa: E501

        :return: The amount of this EscrowRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EscrowRequest.

        Numeric amount to be transferred by the contract in satoshi, amount must be less than 21 BCH.  # noqa: E501

        :param amount: The amount of this EscrowRequest.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if not isinstance(other, EscrowRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EscrowRequest):
            return True

        return self.to_dict() != other.to_dict()
