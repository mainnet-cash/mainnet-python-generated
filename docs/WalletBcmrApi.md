# mainnet.WalletBcmrApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bcmr_add_metadata_registry_auth_chain**](WalletBcmrApi.md#bcmr_add_metadata_registry_auth_chain) | **POST** /wallet/bcmr/add_registry_authchain | Add BCMR metadata registry from autchain, returning the built chain
[**bcmr_add_registry**](WalletBcmrApi.md#bcmr_add_registry) | **POST** /wallet/bcmr/add_registry | Add BCMR registry from parameter
[**bcmr_add_registry_from_uri**](WalletBcmrApi.md#bcmr_add_registry_from_uri) | **POST** /wallet/bcmr/add_registry_from_uri | Reset tracked BCMR registries
[**bcmr_build_auth_chain**](WalletBcmrApi.md#bcmr_build_auth_chain) | **POST** /wallet/bcmr/build_authchain | Build a BCMR authchain
[**bcmr_get_registries**](WalletBcmrApi.md#bcmr_get_registries) | **POST** /wallet/bcmr/get_registries | Get tracked BCMR registries
[**bcmr_get_token_info**](WalletBcmrApi.md#bcmr_get_token_info) | **POST** /wallet/bcmr/get_token_info | Get token info
[**bcmr_reset_registries**](WalletBcmrApi.md#bcmr_reset_registries) | **POST** /wallet/bcmr/reset_registries | Reset tracked BCMR registries


# **bcmr_add_metadata_registry_auth_chain**
> list[AuthChainElement] bcmr_add_metadata_registry_auth_chain(unknown_base_type)

Add BCMR metadata registry from autchain, returning the built chain

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    unknown_base_type = mainnet.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | Add BCMR metadata registry by resolving an authchain, allowing for token info lookup 

    try:
        # Add BCMR metadata registry from autchain, returning the built chain
        api_response = api_instance.bcmr_add_metadata_registry_auth_chain(unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_add_metadata_registry_auth_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Add BCMR metadata registry by resolving an authchain, allowing for token info lookup  | 

### Return type

[**list[AuthChainElement]**](AuthChainElement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_add_registry**
> object bcmr_add_registry(request_body)

Add BCMR registry from parameter

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    request_body = None # dict(str, object) | Add a BCMR registry to the list of tracked, allowing for token info lookup 

    try:
        # Add BCMR registry from parameter
        api_response = api_instance.bcmr_add_registry(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_add_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, object)**](object.md)| Add a BCMR registry to the list of tracked, allowing for token info lookup  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_add_registry_from_uri**
> object bcmr_add_registry_from_uri(unknown_base_type)

Reset tracked BCMR registries

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    unknown_base_type = mainnet.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | Add a BCMR registry from remote URI to the list of tracked, allowing for token info lookup 

    try:
        # Reset tracked BCMR registries
        api_response = api_instance.bcmr_add_registry_from_uri(unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_add_registry_from_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Add a BCMR registry from remote URI to the list of tracked, allowing for token info lookup  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_build_auth_chain**
> list[AuthChainElement] bcmr_build_auth_chain(unknown_base_type)

Build a BCMR authchain

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    unknown_base_type = mainnet.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | Build an authchain - Zeroth-Descendant Transaction Chain, refer to https://github.com/bitjson/chip-bcmr#zeroth-descendant-transaction-chains The authchain in this implementation is specific to resolve to a valid metadata registy 

    try:
        # Build a BCMR authchain
        api_response = api_instance.bcmr_build_auth_chain(unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_build_auth_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Build an authchain - Zeroth-Descendant Transaction Chain, refer to https://github.com/bitjson/chip-bcmr#zeroth-descendant-transaction-chains The authchain in this implementation is specific to resolve to a valid metadata registy  | 

### Return type

[**list[AuthChainElement]**](AuthChainElement.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_get_registries**
> list[dict(str, object)] bcmr_get_registries(request_body=request_body)

Get tracked BCMR registries

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    request_body = None # dict(str, object) | Get tracked BCMR registries.  (optional)

    try:
        # Get tracked BCMR registries
        api_response = api_instance.bcmr_get_registries(request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_get_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, object)**](object.md)| Get tracked BCMR registries.  | [optional] 

### Return type

**list[dict(str, object)]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_get_token_info**
> object bcmr_get_token_info(unknown_base_type)

Get token info

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    unknown_base_type = mainnet.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | Return the token info (the identity snapshot as per BCMR spec) 

    try:
        # Get token info
        api_response = api_instance.bcmr_get_token_info(unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_get_token_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Return the token info (the identity snapshot as per BCMR spec)  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bcmr_reset_registries**
> object bcmr_reset_registries(body=body)

Reset tracked BCMR registries

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
    api_instance = mainnet.WalletBcmrApi(api_client)
    body = None # object | Reset tracked BCMR registries, dropping all token info.  (optional)

    try:
        # Reset tracked BCMR registries
        api_response = api_instance.bcmr_reset_registries(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletBcmrApi->bcmr_reset_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Reset tracked BCMR registries, dropping all token info.  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

