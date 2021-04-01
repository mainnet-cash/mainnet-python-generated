# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.3.8
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mainnet.configuration import Configuration


class WatchAddressRequest(object):
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
        'cashaddr': 'str',
        'url': 'str',
        'type': 'str',
        'recurrence': 'str',
        'duration_sec': 'float'
    }

    attribute_map = {
        'cashaddr': 'cashaddr',
        'url': 'url',
        'type': 'type',
        'recurrence': 'recurrence',
        'duration_sec': 'duration_sec'
    }

    def __init__(self, cashaddr=None, url=None, type='transaction:in,out', recurrence='once', duration_sec=86400, local_vars_configuration=None):  # noqa: E501
        """WatchAddressRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cashaddr = None
        self._url = None
        self._type = None
        self._recurrence = None
        self._duration_sec = None
        self.discriminator = None

        self.cashaddr = cashaddr
        self.url = url
        self.type = type
        if recurrence is not None:
            self.recurrence = recurrence
        if duration_sec is not None:
            self.duration_sec = duration_sec

    @property
    def cashaddr(self):
        """Gets the cashaddr of this WatchAddressRequest.  # noqa: E501

        Cash address to watch   # noqa: E501

        :return: The cashaddr of this WatchAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._cashaddr

    @cashaddr.setter
    def cashaddr(self, cashaddr):
        """Sets the cashaddr of this WatchAddressRequest.

        Cash address to watch   # noqa: E501

        :param cashaddr: The cashaddr of this WatchAddressRequest.  # noqa: E501
        :type cashaddr: str
        """
        if self.local_vars_configuration.client_side_validation and cashaddr is None:  # noqa: E501
            raise ValueError("Invalid value for `cashaddr`, must not be `None`")  # noqa: E501

        self._cashaddr = cashaddr

    @property
    def url(self):
        """Gets the url of this WatchAddressRequest.  # noqa: E501

        Url to be called when configured action is triggered  # noqa: E501

        :return: The url of this WatchAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WatchAddressRequest.

        Url to be called when configured action is triggered  # noqa: E501

        :param url: The url of this WatchAddressRequest.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def type(self):
        """Gets the type of this WatchAddressRequest.  # noqa: E501

        Type of watch operation  # noqa: E501

        :return: The type of this WatchAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WatchAddressRequest.

        Type of watch operation  # noqa: E501

        :param type: The type of this WatchAddressRequest.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["transaction:in", "transaction:out", "transaction:in,out", "balance"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def recurrence(self):
        """Gets the recurrence of this WatchAddressRequest.  # noqa: E501

        Action recurrence. Indicates if webhook should be triggered recurrently until expire or only once  # noqa: E501

        :return: The recurrence of this WatchAddressRequest.  # noqa: E501
        :rtype: str
        """
        return self._recurrence

    @recurrence.setter
    def recurrence(self, recurrence):
        """Sets the recurrence of this WatchAddressRequest.

        Action recurrence. Indicates if webhook should be triggered recurrently until expire or only once  # noqa: E501

        :param recurrence: The recurrence of this WatchAddressRequest.  # noqa: E501
        :type recurrence: str
        """
        allowed_values = ["once", "recurrent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and recurrence not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `recurrence` ({0}), must be one of {1}"  # noqa: E501
                .format(recurrence, allowed_values)
            )

        self._recurrence = recurrence

    @property
    def duration_sec(self):
        """Gets the duration_sec of this WatchAddressRequest.  # noqa: E501

        Duration of the webhook lifetime in seconds before it will expire.  # noqa: E501

        :return: The duration_sec of this WatchAddressRequest.  # noqa: E501
        :rtype: float
        """
        return self._duration_sec

    @duration_sec.setter
    def duration_sec(self, duration_sec):
        """Sets the duration_sec of this WatchAddressRequest.

        Duration of the webhook lifetime in seconds before it will expire.  # noqa: E501

        :param duration_sec: The duration_sec of this WatchAddressRequest.  # noqa: E501
        :type duration_sec: float
        """

        self._duration_sec = duration_sec

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
        if not isinstance(other, WatchAddressRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WatchAddressRequest):
            return True

        return self.to_dict() != other.to_dict()
