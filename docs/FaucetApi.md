# mainnet.FaucetApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses**](FaucetApi.md#get_addresses) | **POST** /faucet/get_addresses | Get addresses to return back or donate the testnet bch and tokens 
[**get_testnet_bch**](FaucetApi.md#get_testnet_bch) | **POST** /faucet/get_testnet_bch | Get testnet bch 
[**get_testnet_slp**](FaucetApi.md#get_testnet_slp) | **POST** /faucet/get_testnet_slp | Get testnet slp tokens 


# **get_addresses**
> GetAddressesResponse get_addresses()

Get addresses to return back or donate the testnet bch and tokens 

### Example

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


# Enter a context with an instance of the API client
with mainnet.ApiClient() as api_client:
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

No authorization required

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


# Enter a context with an instance of the API client
with mainnet.ApiClient() as api_client:
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

No authorization required

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


# Enter a context with an instance of the API client
with mainnet.ApiClient() as api_client:
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

