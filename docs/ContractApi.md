# mainnet.ContractApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_escrow**](ContractApi.md#create_escrow) | **POST** /contract/escrow/create | Create an escrow contract
[**escrow_fn**](ContractApi.md#escrow_fn) | **POST** /contract/escrow/call | Finalize an escrow contract
[**escrow_utxos**](ContractApi.md#escrow_utxos) | **POST** /contract/escrow/utxos | List specific utxos in a contract


# **create_escrow**
> ContractResponse create_escrow(escrow_request)

Create an escrow contract

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
    api_instance = mainnet.ContractApi(api_client)
    escrow_request = mainnet.EscrowRequest() # EscrowRequest | Request a new escrow contract

    try:
        # Create an escrow contract
        api_response = api_instance.create_escrow(escrow_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->create_escrow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escrow_request** | [**EscrowRequest**](EscrowRequest.md)| Request a new escrow contract | 

### Return type

[**ContractResponse**](ContractResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **escrow_fn**
> ContractFnResponse escrow_fn(contract_fn_request)

Finalize an escrow contract

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
    api_instance = mainnet.ContractApi(api_client)
    contract_fn_request = mainnet.ContractFnRequest() # ContractFnRequest | null

    try:
        # Finalize an escrow contract
        api_response = api_instance.escrow_fn(contract_fn_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->escrow_fn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_fn_request** | [**ContractFnRequest**](ContractFnRequest.md)| null | 

### Return type

[**ContractFnResponse**](ContractFnResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **escrow_utxos**
> UtxoResponse escrow_utxos(contract)

List specific utxos in a contract

Returns all UTXOs that can be spent by the  contract. Both confirmed and unconfirmed UTXOs are included. 

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
    api_instance = mainnet.ContractApi(api_client)
    contract = mainnet.Contract() # Contract | 

    try:
        # List specific utxos in a contract
        api_response = api_instance.escrow_utxos(contract)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractApi->escrow_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | [**Contract**](Contract.md)|  | 

### Return type

[**UtxoResponse**](UtxoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

