# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 2.4.1
    Contact: hello@mainnet.cash
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mainnet.api_client import ApiClient
from mainnet.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WalletUtilApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def util_decode_transaction(self, util_decode_transaction_request, **kwargs):  # noqa: E501
        """Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.util_decode_transaction(util_decode_transaction_request, async_req=True)
        >>> result = thread.get()

        :param util_decode_transaction_request: Request to decode a transaction  (required)
        :type util_decode_transaction_request: UtilDecodeTransactionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ElectrumRawTransaction
        """
        kwargs['_return_http_data_only'] = True
        return self.util_decode_transaction_with_http_info(util_decode_transaction_request, **kwargs)  # noqa: E501

    def util_decode_transaction_with_http_info(self, util_decode_transaction_request, **kwargs):  # noqa: E501
        """Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.util_decode_transaction_with_http_info(util_decode_transaction_request, async_req=True)
        >>> result = thread.get()

        :param util_decode_transaction_request: Request to decode a transaction  (required)
        :type util_decode_transaction_request: UtilDecodeTransactionRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ElectrumRawTransaction, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'util_decode_transaction_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method util_decode_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'util_decode_transaction_request' is set
        if self.api_client.client_side_validation and ('util_decode_transaction_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['util_decode_transaction_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `util_decode_transaction_request` when calling `util_decode_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'util_decode_transaction_request' in local_var_params:
            body_params = local_var_params['util_decode_transaction_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallet/util/decode_transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ElectrumRawTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def util_get_raw_transaction(self, unknown_base_type, **kwargs):  # noqa: E501
        """Get bitcoin raw transaction  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.util_get_raw_transaction(unknown_base_type, async_req=True)
        >>> result = thread.get()

        :param unknown_base_type: Request to get raw transaction  (required)
        :type unknown_base_type: UNKNOWN_BASE_TYPE
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AnyOfobjectElectrumRawTransaction
        """
        kwargs['_return_http_data_only'] = True
        return self.util_get_raw_transaction_with_http_info(unknown_base_type, **kwargs)  # noqa: E501

    def util_get_raw_transaction_with_http_info(self, unknown_base_type, **kwargs):  # noqa: E501
        """Get bitcoin raw transaction  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.util_get_raw_transaction_with_http_info(unknown_base_type, async_req=True)
        >>> result = thread.get()

        :param unknown_base_type: Request to get raw transaction  (required)
        :type unknown_base_type: UNKNOWN_BASE_TYPE
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AnyOfobjectElectrumRawTransaction, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'unknown_base_type'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method util_get_raw_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'unknown_base_type' is set
        if self.api_client.client_side_validation and ('unknown_base_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['unknown_base_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `unknown_base_type` when calling `util_get_raw_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'unknown_base_type' in local_var_params:
            body_params = local_var_params['unknown_base_type']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/wallet/util/get_raw_transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnyOfobjectElectrumRawTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
