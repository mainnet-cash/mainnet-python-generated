# mainnet.UtilApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](UtilApi.md#convert) | **POST** /util/convert | convert between units
[**get_addrs_by_xpub_key**](UtilApi.md#get_addrs_by_xpub_key) | **POST** /util/get_addrs_by_xpubkey | Derive heristic determined addresses from an extended public key, per BIP32
[**get_xpub_key_info**](UtilApi.md#get_xpub_key_info) | **POST** /util/get_xpubkey_info | Decode information about an extended public key, per BIP32


# **convert**
> float convert(convert_request=convert_request)

convert between units

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
    api_instance = mainnet.UtilApi(api_client)
    convert_request = mainnet.ConvertRequest() # ConvertRequest |  (optional)

    try:
        # convert between units
        api_response = api_instance.convert(convert_request=convert_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UtilApi->convert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_request** | [**ConvertRequest**](ConvertRequest.md)|  | [optional] 

### Return type

**float**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addrs_by_xpub_key**
> list[AnyOfstring] get_addrs_by_xpub_key(get_addrs_by_xpub_key_request=get_addrs_by_xpub_key_request)

Derive heristic determined addresses from an extended public key, per BIP32

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
    api_instance = mainnet.UtilApi(api_client)
    get_addrs_by_xpub_key_request = mainnet.GetAddrsByXpubKeyRequest() # GetAddrsByXpubKeyRequest |  (optional)

    try:
        # Derive heristic determined addresses from an extended public key, per BIP32
        api_response = api_instance.get_addrs_by_xpub_key(get_addrs_by_xpub_key_request=get_addrs_by_xpub_key_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UtilApi->get_addrs_by_xpub_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_addrs_by_xpub_key_request** | [**GetAddrsByXpubKeyRequest**](GetAddrsByXpubKeyRequest.md)|  | [optional] 

### Return type

[**list[AnyOfstring]**](AnyOfstring.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xpub_key_info**
> GetXpubKeyInfoResponse get_xpub_key_info(get_xpub_key_info_request)

Decode information about an extended public key, per BIP32

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
    api_instance = mainnet.UtilApi(api_client)
    get_xpub_key_info_request = mainnet.GetXpubKeyInfoRequest() # GetXpubKeyInfoRequest | Decode information about an extended public key, per BIP32

    try:
        # Decode information about an extended public key, per BIP32
        api_response = api_instance.get_xpub_key_info(get_xpub_key_info_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UtilApi->get_xpub_key_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_xpub_key_info_request** | [**GetXpubKeyInfoRequest**](GetXpubKeyInfoRequest.md)| Decode information about an extended public key, per BIP32 | 

### Return type

[**GetXpubKeyInfoResponse**](GetXpubKeyInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

