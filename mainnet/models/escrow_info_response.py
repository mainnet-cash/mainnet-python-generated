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


class EscrowInfoResponse(object):
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
        'script': 'str',
        'parameters': 'list[str]',
        'cashaddr': 'str',
        'buyer_addr': 'object',
        'arbiter_addr': 'object',
        'seller_addr': 'object',
        'amount': 'float',
        'nonce': 'float'
    }

    attribute_map = {
        'escrow_contract_id': 'escrowContractId',
        'script': 'script',
        'parameters': 'parameters',
        'cashaddr': 'cashaddr',
        'buyer_addr': 'buyerAddr',
        'arbiter_addr': 'arbiterAddr',
        'seller_addr': 'sellerAddr',
        'amount': 'amount',
        'nonce': 'nonce'
    }

    def __init__(self, escrow_contract_id=None, script=None, parameters=None, cashaddr=None, buyer_addr=None, arbiter_addr=None, seller_addr=None, amount=None, nonce=None, local_vars_configuration=None):  # noqa: E501
        """EscrowInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._escrow_contract_id = None
        self._script = None
        self._parameters = None
        self._cashaddr = None
        self._buyer_addr = None
        self._arbiter_addr = None
        self._seller_addr = None
        self._amount = None
        self._nonce = None
        self.discriminator = None

        if escrow_contract_id is not None:
            self.escrow_contract_id = escrow_contract_id
        if script is not None:
            self.script = script
        if parameters is not None:
            self.parameters = parameters
        if cashaddr is not None:
            self.cashaddr = cashaddr
        self.buyer_addr = buyer_addr
        self.arbiter_addr = arbiter_addr
        self.seller_addr = seller_addr
        if amount is not None:
            self.amount = amount
        if nonce is not None:
            self.nonce = nonce

    @property
    def escrow_contract_id(self):
        """Gets the escrow_contract_id of this EscrowInfoResponse.  # noqa: E501

        serialized escrow contract   # noqa: E501

        :return: The escrow_contract_id of this EscrowInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._escrow_contract_id

    @escrow_contract_id.setter
    def escrow_contract_id(self, escrow_contract_id):
        """Sets the escrow_contract_id of this EscrowInfoResponse.

        serialized escrow contract   # noqa: E501

        :param escrow_contract_id: The escrow_contract_id of this EscrowInfoResponse.  # noqa: E501
        :type escrow_contract_id: str
        """

        self._escrow_contract_id = escrow_contract_id

    @property
    def script(self):
        """Gets the script of this EscrowInfoResponse.  # noqa: E501

        The escrow contract in cashscript syntax   # noqa: E501

        :return: The script of this EscrowInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this EscrowInfoResponse.

        The escrow contract in cashscript syntax   # noqa: E501

        :param script: The script of this EscrowInfoResponse.  # noqa: E501
        :type script: str
        """

        self._script = script

    @property
    def parameters(self):
        """Gets the parameters of this EscrowInfoResponse.  # noqa: E501

        Parameters passed when the contract was created  # noqa: E501

        :return: The parameters of this EscrowInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this EscrowInfoResponse.

        Parameters passed when the contract was created  # noqa: E501

        :param parameters: The parameters of this EscrowInfoResponse.  # noqa: E501
        :type parameters: list[str]
        """

        self._parameters = parameters

    @property
    def cashaddr(self):
        """Gets the cashaddr of this EscrowInfoResponse.  # noqa: E501


        :return: The cashaddr of this EscrowInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this EscrowInfoResponse.


        :param cashaddr: The cashaddr of this EscrowInfoResponse.  # noqa: E501
        :type cashaddr: str
        """

        self._cashaddr = cashaddr

    @property
    def buyer_addr(self):
        """Gets the buyer_addr of this EscrowInfoResponse.  # noqa: E501

        The cashaddress of the buyer  # noqa: E501

        :return: The buyer_addr of this EscrowInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._buyer_addr

    @buyer_addr.setter
    def buyer_addr(self, buyer_addr):
        """Sets the buyer_addr of this EscrowInfoResponse.

        The cashaddress of the buyer  # noqa: E501

        :param buyer_addr: The buyer_addr of this EscrowInfoResponse.  # noqa: E501
        :type buyer_addr: object
        """

        self._buyer_addr = buyer_addr

    @property
    def arbiter_addr(self):
        """Gets the arbiter_addr of this EscrowInfoResponse.  # noqa: E501

        The cashaddress of the arbiter  # noqa: E501

        :return: The arbiter_addr of this EscrowInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._arbiter_addr

    @arbiter_addr.setter
    def arbiter_addr(self, arbiter_addr):
        """Sets the arbiter_addr of this EscrowInfoResponse.

        The cashaddress of the arbiter  # noqa: E501

        :param arbiter_addr: The arbiter_addr of this EscrowInfoResponse.  # noqa: E501
        :type arbiter_addr: object
        """

        self._arbiter_addr = arbiter_addr

    @property
    def seller_addr(self):
        """Gets the seller_addr of this EscrowInfoResponse.  # noqa: E501

        The cashaddress of the seller  # noqa: E501

        :return: The seller_addr of this EscrowInfoResponse.  # noqa: E501
        :rtype: object
        """
        return self._seller_addr

    @seller_addr.setter
    def seller_addr(self, seller_addr):
        """Sets the seller_addr of this EscrowInfoResponse.

        The cashaddress of the seller  # noqa: E501

        :param seller_addr: The seller_addr of this EscrowInfoResponse.  # noqa: E501
        :type seller_addr: object
        """

        self._seller_addr = seller_addr

    @property
    def amount(self):
        """Gets the amount of this EscrowInfoResponse.  # noqa: E501

        Numeric amount to be transferred by the contract in satoshi, amount must be less than 21 BCH.  # noqa: E501

        :return: The amount of this EscrowInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EscrowInfoResponse.

        Numeric amount to be transferred by the contract in satoshi, amount must be less than 21 BCH.  # noqa: E501

        :param amount: The amount of this EscrowInfoResponse.  # noqa: E501
        :type amount: float
        """

        self._amount = amount

    @property
    def nonce(self):
        """Gets the nonce of this EscrowInfoResponse.  # noqa: E501

        A unique number used once for each instance of a contract.  # noqa: E501

        :return: The nonce of this EscrowInfoResponse.  # noqa: E501
        :rtype: float
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this EscrowInfoResponse.

        A unique number used once for each instance of a contract.  # noqa: E501

        :param nonce: The nonce of this EscrowInfoResponse.  # noqa: E501
        :type nonce: float
        """

        self._nonce = nonce

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
        if not isinstance(other, EscrowInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EscrowInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
