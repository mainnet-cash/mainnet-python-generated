# coding: utf-8

"""
    Mainnet Cash

    A developer friendly bitcoin cash wallet api  This API is currently in *active* development, breaking changes may be made prior to official release of version 1.0.0.   # noqa: E501

    The version of the OpenAPI document: 0.4.11
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


class SmartbchContractApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def smart_bch_contract_call(self, smart_bch_contract_fn_call_request, **kwargs):  # noqa: E501
        """Call a SmartBch contract function  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_call(smart_bch_contract_fn_call_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_fn_call_request: (required)
        :type smart_bch_contract_fn_call_request: SmartBchContractFnCallRequest
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
        :rtype: SmartBchContractFnCallResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.smart_bch_contract_call_with_http_info(smart_bch_contract_fn_call_request, **kwargs)  # noqa: E501

    def smart_bch_contract_call_with_http_info(self, smart_bch_contract_fn_call_request, **kwargs):  # noqa: E501
        """Call a SmartBch contract function  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_call_with_http_info(smart_bch_contract_fn_call_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_fn_call_request: (required)
        :type smart_bch_contract_fn_call_request: SmartBchContractFnCallRequest
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
        :rtype: tuple(SmartBchContractFnCallResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'smart_bch_contract_fn_call_request'
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
                    " to method smart_bch_contract_call" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'smart_bch_contract_fn_call_request' is set
        if self.api_client.client_side_validation and ('smart_bch_contract_fn_call_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['smart_bch_contract_fn_call_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `smart_bch_contract_fn_call_request` when calling `smart_bch_contract_call`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_bch_contract_fn_call_request' in local_var_params:
            body_params = local_var_params['smart_bch_contract_fn_call_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartbch/contract/call', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartBchContractFnCallResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def smart_bch_contract_create(self, smart_bch_contract_request, **kwargs):  # noqa: E501
        """Create a SmartBch contractId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_create(smart_bch_contract_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_request: Create a SmartBch contractId (required)
        :type smart_bch_contract_request: SmartBchContractRequest
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
        :rtype: SmartBchContractResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.smart_bch_contract_create_with_http_info(smart_bch_contract_request, **kwargs)  # noqa: E501

    def smart_bch_contract_create_with_http_info(self, smart_bch_contract_request, **kwargs):  # noqa: E501
        """Create a SmartBch contractId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_create_with_http_info(smart_bch_contract_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_request: Create a SmartBch contractId (required)
        :type smart_bch_contract_request: SmartBchContractRequest
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
        :rtype: tuple(SmartBchContractResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'smart_bch_contract_request'
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
                    " to method smart_bch_contract_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'smart_bch_contract_request' is set
        if self.api_client.client_side_validation and ('smart_bch_contract_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['smart_bch_contract_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `smart_bch_contract_request` when calling `smart_bch_contract_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_bch_contract_request' in local_var_params:
            body_params = local_var_params['smart_bch_contract_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartbch/contract/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartBchContractResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def smart_bch_contract_deploy(self, smart_bch_contract_deploy_request, **kwargs):  # noqa: E501
        """Request to deploy a SmartBch contract  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_deploy(smart_bch_contract_deploy_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_deploy_request: Request to deploy a SmartBch contract (required)
        :type smart_bch_contract_deploy_request: SmartBchContractDeployRequest
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
        :rtype: SmartBchContractDeployResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.smart_bch_contract_deploy_with_http_info(smart_bch_contract_deploy_request, **kwargs)  # noqa: E501

    def smart_bch_contract_deploy_with_http_info(self, smart_bch_contract_deploy_request, **kwargs):  # noqa: E501
        """Request to deploy a SmartBch contract  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_deploy_with_http_info(smart_bch_contract_deploy_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_deploy_request: Request to deploy a SmartBch contract (required)
        :type smart_bch_contract_deploy_request: SmartBchContractDeployRequest
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
        :rtype: tuple(SmartBchContractDeployResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'smart_bch_contract_deploy_request'
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
                    " to method smart_bch_contract_deploy" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'smart_bch_contract_deploy_request' is set
        if self.api_client.client_side_validation and ('smart_bch_contract_deploy_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['smart_bch_contract_deploy_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `smart_bch_contract_deploy_request` when calling `smart_bch_contract_deploy`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_bch_contract_deploy_request' in local_var_params:
            body_params = local_var_params['smart_bch_contract_deploy_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartbch/contract/deploy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartBchContractDeployResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def smart_bch_contract_estimate_gas(self, smart_bch_contract_estimate_gas_request, **kwargs):  # noqa: E501
        """Estimate the gas for a contract interaction function given the arguments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_estimate_gas(smart_bch_contract_estimate_gas_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_estimate_gas_request: (required)
        :type smart_bch_contract_estimate_gas_request: SmartBchContractEstimateGasRequest
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
        :rtype: SmartBchContractEstimateGasResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.smart_bch_contract_estimate_gas_with_http_info(smart_bch_contract_estimate_gas_request, **kwargs)  # noqa: E501

    def smart_bch_contract_estimate_gas_with_http_info(self, smart_bch_contract_estimate_gas_request, **kwargs):  # noqa: E501
        """Estimate the gas for a contract interaction function given the arguments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_estimate_gas_with_http_info(smart_bch_contract_estimate_gas_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_estimate_gas_request: (required)
        :type smart_bch_contract_estimate_gas_request: SmartBchContractEstimateGasRequest
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
        :rtype: tuple(SmartBchContractEstimateGasResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'smart_bch_contract_estimate_gas_request'
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
                    " to method smart_bch_contract_estimate_gas" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'smart_bch_contract_estimate_gas_request' is set
        if self.api_client.client_side_validation and ('smart_bch_contract_estimate_gas_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['smart_bch_contract_estimate_gas_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `smart_bch_contract_estimate_gas_request` when calling `smart_bch_contract_estimate_gas`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_bch_contract_estimate_gas_request' in local_var_params:
            body_params = local_var_params['smart_bch_contract_estimate_gas_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartbch/contract/estimate_gas', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartBchContractEstimateGasResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def smart_bch_contract_info(self, smart_bch_contract_info_request, **kwargs):  # noqa: E501
        """Get information about a SmartBch contract from the contractId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_info(smart_bch_contract_info_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_info_request: Request parsed information regarding a SmartBch contract from the smartBchContractId (required)
        :type smart_bch_contract_info_request: SmartBchContractInfoRequest
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
        :rtype: SmartBchContractInfoResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.smart_bch_contract_info_with_http_info(smart_bch_contract_info_request, **kwargs)  # noqa: E501

    def smart_bch_contract_info_with_http_info(self, smart_bch_contract_info_request, **kwargs):  # noqa: E501
        """Get information about a SmartBch contract from the contractId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.smart_bch_contract_info_with_http_info(smart_bch_contract_info_request, async_req=True)
        >>> result = thread.get()

        :param smart_bch_contract_info_request: Request parsed information regarding a SmartBch contract from the smartBchContractId (required)
        :type smart_bch_contract_info_request: SmartBchContractInfoRequest
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
        :rtype: tuple(SmartBchContractInfoResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'smart_bch_contract_info_request'
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
                    " to method smart_bch_contract_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'smart_bch_contract_info_request' is set
        if self.api_client.client_side_validation and ('smart_bch_contract_info_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['smart_bch_contract_info_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `smart_bch_contract_info_request` when calling `smart_bch_contract_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'smart_bch_contract_info_request' in local_var_params:
            body_params = local_var_params['smart_bch_contract_info_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/smartbch/contract/info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SmartBchContractInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
