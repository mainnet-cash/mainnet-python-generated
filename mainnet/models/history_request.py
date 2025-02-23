# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.6.3
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class HistoryRequest(object):
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
        'unit': 'str',
        'from_height': 'float',
        'to_height': 'float',
        'start': 'float',
        'count': 'float'
    }

    attribute_map = {
        'wallet_id': 'walletId',
        'unit': 'unit',
        'from_height': 'fromHeight',
        'to_height': 'toHeight',
        'start': 'start',
        'count': 'count'
    }

    def __init__(self, wallet_id=None, unit='sat', from_height=0, to_height=-1, start=0, count=None, local_vars_configuration=None):  # noqa: E501
        """HistoryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wallet_id = None
        self._unit = None
        self._from_height = None
        self._to_height = None
        self._start = None
        self._count = None
        self.discriminator = None

        self.wallet_id = wallet_id
        if unit is not None:
            self.unit = unit
        if from_height is not None:
            self.from_height = from_height
        if to_height is not None:
            self.to_height = to_height
        if start is not None:
            self.start = start
        if count is not None:
            self.count = count

    @property
    def wallet_id(self):
        """Gets the wallet_id of this HistoryRequest.  # noqa: E501

        The walletId to get a history for.   # noqa: E501

        :return: The wallet_id of this HistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this HistoryRequest.

        The walletId to get a history for.   # noqa: E501

        :param wallet_id: The wallet_id of this HistoryRequest.  # noqa: E501
        :type wallet_id: str
        """
        if self.local_vars_configuration.client_side_validation and wallet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `wallet_id`, must not be `None`")  # noqa: E501

        self._wallet_id = wallet_id

    @property
    def unit(self):
        """Gets the unit of this HistoryRequest.  # noqa: E501

        Unit of account for running balance.  # noqa: E501

        :return: The unit of this HistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this HistoryRequest.

        Unit of account for running balance.  # noqa: E501

        :param unit: The unit of this HistoryRequest.  # noqa: E501
        :type unit: str
        """
        allowed_values = ["bch", "BCH", "usd", "USD", "bit", "bits", "sat", "SAT", "sats", "satoshi", "satoshis"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def from_height(self):
        """Gets the from_height of this HistoryRequest.  # noqa: E501

        optional, if set, history will be limited. Default 0  # noqa: E501

        :return: The from_height of this HistoryRequest.  # noqa: E501
        :rtype: float
        """
        return self._from_height

    @from_height.setter
    def from_height(self, from_height):
        """Sets the from_height of this HistoryRequest.

        optional, if set, history will be limited. Default 0  # noqa: E501

        :param from_height: The from_height of this HistoryRequest.  # noqa: E501
        :type from_height: float
        """

        self._from_height = from_height

    @property
    def to_height(self):
        """Gets the to_height of this HistoryRequest.  # noqa: E501

        optional, if set, history will be limited. Default -1, meaning that all history items will be returned, including mempool  # noqa: E501

        :return: The to_height of this HistoryRequest.  # noqa: E501
        :rtype: float
        """
        return self._to_height

    @to_height.setter
    def to_height(self, to_height):
        """Sets the to_height of this HistoryRequest.

        optional, if set, history will be limited. Default -1, meaning that all history items will be returned, including mempool  # noqa: E501

        :param to_height: The to_height of this HistoryRequest.  # noqa: E501
        :type to_height: float
        """

        self._to_height = to_height

    @property
    def start(self):
        """Gets the start of this HistoryRequest.  # noqa: E501

        optional, if set, the result set will be paginated with offset `start`. Default 0  # noqa: E501

        :return: The start of this HistoryRequest.  # noqa: E501
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this HistoryRequest.

        optional, if set, the result set will be paginated with offset `start`. Default 0  # noqa: E501

        :param start: The start of this HistoryRequest.  # noqa: E501
        :type start: float
        """

        self._start = start

    @property
    def count(self):
        """Gets the count of this HistoryRequest.  # noqa: E501

        optional, if set, the result set will be paginated with `count`. Default -1, meaning that all history items will be returned  # noqa: E501

        :return: The count of this HistoryRequest.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this HistoryRequest.

        optional, if set, the result set will be paginated with `count`. Default -1, meaning that all history items will be returned  # noqa: E501

        :param count: The count of this HistoryRequest.  # noqa: E501
        :type count: float
        """

        self._count = count

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
        if not isinstance(other, HistoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoryRequest):
            return True

        return self.to_dict() != other.to_dict()
