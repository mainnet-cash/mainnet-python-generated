# mainnet.FaucetApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses**](FaucetApi.md#get_addresses) | **POST** /faucet/get_addresses | Get addresses to return back or donate the testnet bch and tokens 
[**get_testnet_bch**](FaucetApi.md#get_testnet_bch) | **POST** /faucet/get_testnet_bch | Get testnet bch 
[**get_testnet_sbch**](FaucetApi.md#get_testnet_sbch) | **POST** /faucet/get_testnet_sbch | Request testnet SmartBCH funds. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 0.1 BCH, the request will fail. Otherwise the address will be topped up to 0.1 BCH. 
[**get_testnet_sep20**](FaucetApi.md#get_testnet_sep20) | **POST** /faucet/get_testnet_sep20 | Request testnet SmartBch SEP20 tokens. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 10 tokens of requested kind, the request will fail. Otherwise the address will be topped up to 10 tokens. 
[**get_testnet_slp**](FaucetApi.md#get_testnet_slp) | **POST** /faucet/get_testnet_slp | Get testnet slp tokens 


# **get_addresses**
> GetAddressesResponse get_addresses()

Get addresses to return back or donate the testnet bch and tokens 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.FaucetApi(api_client)
    
    try:
        # Get addresses to return back or donate the testnet bch and tokens 
        api_response = api_instance.get_addresses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaucetApi->get_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAddressesResponse**](GetAddressesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testnet_bch**
> GetTestnetBchResponse get_testnet_bch(get_testnet_bch_request)

Get testnet bch 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.FaucetApi(api_client)
    get_testnet_bch_request = mainnet.GetTestnetBchRequest() # GetTestnetBchRequest | Request to bch faucet 

    try:
        # Get testnet bch 
        api_response = api_instance.get_testnet_bch(get_testnet_bch_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaucetApi->get_testnet_bch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_testnet_bch_request** | [**GetTestnetBchRequest**](GetTestnetBchRequest.md)| Request to bch faucet  | 

### Return type

[**GetTestnetBchResponse**](GetTestnetBchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testnet_sbch**
> GetTestnetSbchResponse get_testnet_sbch(get_testnet_sbch_request)

Request testnet SmartBCH funds. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 0.1 BCH, the request will fail. Otherwise the address will be topped up to 0.1 BCH. 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.FaucetApi(api_client)
    get_testnet_sbch_request = mainnet.GetTestnetSbchRequest() # GetTestnetSbchRequest | Request to bch faucet 

    try:
        # Request testnet SmartBCH funds. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 0.1 BCH, the request will fail. Otherwise the address will be topped up to 0.1 BCH. 
        api_response = api_instance.get_testnet_sbch(get_testnet_sbch_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaucetApi->get_testnet_sbch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_testnet_sbch_request** | [**GetTestnetSbchRequest**](GetTestnetSbchRequest.md)| Request to bch faucet  | 

### Return type

[**GetTestnetSbchResponse**](GetTestnetSbchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testnet_sep20**
> GetTestnetSep20Response get_testnet_sep20(get_testnet_sep20_request)

Request testnet SmartBch SEP20 tokens. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 10 tokens of requested kind, the request will fail. Otherwise the address will be topped up to 10 tokens. 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.FaucetApi(api_client)
    get_testnet_sep20_request = mainnet.GetTestnetSep20Request() # GetTestnetSep20Request | Request to SEP20 faucet 

    try:
        # Request testnet SmartBch SEP20 tokens. The request is enqueued and served within 1-3 block confirmations. If the target address holds more that 10 tokens of requested kind, the request will fail. Otherwise the address will be topped up to 10 tokens. 
        api_response = api_instance.get_testnet_sep20(get_testnet_sep20_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaucetApi->get_testnet_sep20: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_testnet_sep20_request** | [**GetTestnetSep20Request**](GetTestnetSep20Request.md)| Request to SEP20 faucet  | 

### Return type

[**GetTestnetSep20Response**](GetTestnetSep20Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_testnet_slp**
> GetTestnetSlpResponse get_testnet_slp(get_testnet_slp_request)

Get testnet slp tokens 

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import mainnet
from mainnet.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://rest-unstable.mainnet.cash
# See configuration.py for a list of all supported configuration parameters.
configuration = mainnet.Configuration(
    host = "https://rest-unstable.mainnet.cash"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = mainnet.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with mainnet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mainnet.FaucetApi(api_client)
    get_testnet_slp_request = mainnet.GetTestnetSlpRequest() # GetTestnetSlpRequest | Request to slp faucet 

    try:
        # Get testnet slp tokens 
        api_response = api_instance.get_testnet_slp(get_testnet_slp_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaucetApi->get_testnet_slp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_testnet_slp_request** | [**GetTestnetSlpRequest**](GetTestnetSlpRequest.md)| Request to slp faucet  | 

### Return type

[**GetTestnetSlpResponse**](GetTestnetSlpResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

