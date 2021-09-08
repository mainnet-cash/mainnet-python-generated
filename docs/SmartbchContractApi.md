# mainnet.SmartbchContractApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_bch_contract_call**](SmartbchContractApi.md#smart_bch_contract_call) | **POST** /smartbch/contract/call | Call a SmartBch contract function
[**smart_bch_contract_create**](SmartbchContractApi.md#smart_bch_contract_create) | **POST** /smartbch/contract/create | Create a SmartBch contractId
[**smart_bch_contract_deploy**](SmartbchContractApi.md#smart_bch_contract_deploy) | **POST** /smartbch/contract/deploy | Request to deploy a SmartBch contract
[**smart_bch_contract_estimate_gas**](SmartbchContractApi.md#smart_bch_contract_estimate_gas) | **POST** /smartbch/contract/estimate_gas | Estimate the gas for a contract interaction function given the arguments
[**smart_bch_contract_info**](SmartbchContractApi.md#smart_bch_contract_info) | **POST** /smartbch/contract/info | Get information about a SmartBch contract from the contractId


# **smart_bch_contract_call**
> SmartBchContractFnCallResponse smart_bch_contract_call(smart_bch_contract_fn_call_request)

Call a SmartBch contract function

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
    api_instance = mainnet.SmartbchContractApi(api_client)
    smart_bch_contract_fn_call_request = mainnet.SmartBchContractFnCallRequest() # SmartBchContractFnCallRequest | 

    try:
        # Call a SmartBch contract function
        api_response = api_instance.smart_bch_contract_call(smart_bch_contract_fn_call_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchContractApi->smart_bch_contract_call: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_contract_fn_call_request** | [**SmartBchContractFnCallRequest**](SmartBchContractFnCallRequest.md)|  | 

### Return type

[**SmartBchContractFnCallResponse**](SmartBchContractFnCallResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_bch_contract_create**
> SmartBchContractResponse smart_bch_contract_create(smart_bch_contract_request)

Create a SmartBch contractId

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
    api_instance = mainnet.SmartbchContractApi(api_client)
    smart_bch_contract_request = mainnet.SmartBchContractRequest() # SmartBchContractRequest | Create a SmartBch contractId

    try:
        # Create a SmartBch contractId
        api_response = api_instance.smart_bch_contract_create(smart_bch_contract_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchContractApi->smart_bch_contract_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_contract_request** | [**SmartBchContractRequest**](SmartBchContractRequest.md)| Create a SmartBch contractId | 

### Return type

[**SmartBchContractResponse**](SmartBchContractResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_bch_contract_deploy**
> SmartBchContractDeployResponse smart_bch_contract_deploy(smart_bch_contract_deploy_request)

Request to deploy a SmartBch contract

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
    api_instance = mainnet.SmartbchContractApi(api_client)
    smart_bch_contract_deploy_request = mainnet.SmartBchContractDeployRequest() # SmartBchContractDeployRequest | Request to deploy a SmartBch contract

    try:
        # Request to deploy a SmartBch contract
        api_response = api_instance.smart_bch_contract_deploy(smart_bch_contract_deploy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchContractApi->smart_bch_contract_deploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_contract_deploy_request** | [**SmartBchContractDeployRequest**](SmartBchContractDeployRequest.md)| Request to deploy a SmartBch contract | 

### Return type

[**SmartBchContractDeployResponse**](SmartBchContractDeployResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_bch_contract_estimate_gas**
> SmartBchContractEstimateGasResponse smart_bch_contract_estimate_gas(smart_bch_contract_estimate_gas_request)

Estimate the gas for a contract interaction function given the arguments

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
    api_instance = mainnet.SmartbchContractApi(api_client)
    smart_bch_contract_estimate_gas_request = mainnet.SmartBchContractEstimateGasRequest() # SmartBchContractEstimateGasRequest | 

    try:
        # Estimate the gas for a contract interaction function given the arguments
        api_response = api_instance.smart_bch_contract_estimate_gas(smart_bch_contract_estimate_gas_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchContractApi->smart_bch_contract_estimate_gas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_contract_estimate_gas_request** | [**SmartBchContractEstimateGasRequest**](SmartBchContractEstimateGasRequest.md)|  | 

### Return type

[**SmartBchContractEstimateGasResponse**](SmartBchContractEstimateGasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smart_bch_contract_info**
> SmartBchContractInfoResponse smart_bch_contract_info(smart_bch_contract_info_request)

Get information about a SmartBch contract from the contractId

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
    api_instance = mainnet.SmartbchContractApi(api_client)
    smart_bch_contract_info_request = mainnet.SmartBchContractInfoRequest() # SmartBchContractInfoRequest | Request parsed information regarding a SmartBch contract from the smartBchContractId

    try:
        # Get information about a SmartBch contract from the contractId
        api_response = api_instance.smart_bch_contract_info(smart_bch_contract_info_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchContractApi->smart_bch_contract_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_contract_info_request** | [**SmartBchContractInfoRequest**](SmartBchContractInfoRequest.md)| Request parsed information regarding a SmartBch contract from the smartBchContractId | 

### Return type

[**SmartBchContractInfoResponse**](SmartBchContractInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

