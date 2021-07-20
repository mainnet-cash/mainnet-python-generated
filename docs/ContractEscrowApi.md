# mainnet.ContractEscrowApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_escrow**](ContractEscrowApi.md#create_escrow) | **POST** /contract/escrow/create | Create an escrow contract
[**escrow_fn**](ContractEscrowApi.md#escrow_fn) | **POST** /contract/escrow/call | Finalize an escrow contract
[**escrow_info**](ContractEscrowApi.md#escrow_info) | **POST** /contract/escrow/info | Get information about an escrow contract from the escrowContractId
[**escrow_utxos**](ContractEscrowApi.md#escrow_utxos) | **POST** /contract/escrow/utxos | List specific utxos on any escrow contract


# **create_escrow**
> EscrowResponse create_escrow(escrow_request)

Create an escrow contract

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
    api_instance = mainnet.ContractEscrowApi(api_client)
    escrow_request = mainnet.EscrowRequest() # EscrowRequest | Request a new escrow contract from a template

    try:
        # Create an escrow contract
        api_response = api_instance.create_escrow(escrow_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractEscrowApi->create_escrow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escrow_request** | [**EscrowRequest**](EscrowRequest.md)| Request a new escrow contract from a template | 

### Return type

[**EscrowResponse**](EscrowResponse.md)

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

# **escrow_fn**
> ContractFnResponse escrow_fn(escrow_fn_request)

Finalize an escrow contract

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
    api_instance = mainnet.ContractEscrowApi(api_client)
    escrow_fn_request = mainnet.EscrowFnRequest() # EscrowFnRequest | 

    try:
        # Finalize an escrow contract
        api_response = api_instance.escrow_fn(escrow_fn_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractEscrowApi->escrow_fn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escrow_fn_request** | [**EscrowFnRequest**](EscrowFnRequest.md)|  | 

### Return type

[**ContractFnResponse**](ContractFnResponse.md)

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

# **escrow_info**
> EscrowInfoResponse escrow_info(escrow_info_request)

Get information about an escrow contract from the escrowContractId

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
    api_instance = mainnet.ContractEscrowApi(api_client)
    escrow_info_request = {"escrowContractId":"escrowContract:testnet:WW1Ob2RHVnpkRHB4ZWpBd2NHczViR1p6TUdzNVpqVjJaak5xT0dnMk5uRm1iWEZoWjJzNGJtTTFObVZzY1RSa2RqST06WW1Ob2RHVnpkRHB4Y201c2RYVm5aVFUyWVdoNGMzazJjSEJzY1RRemNuWmhOMnMyY3psa2EyNTFOSEExTWpjNFlXZz06WW1Ob2RHVnpkRHB4ZW5Od1kzbDNlRzF0TkdaeGFHWTVhMnB5YTI1eVl6Tm5jbk4yTW5aMWEyVnhlV3B4YkdFd2JuUT06TVRBd01EQT0=:TVRVNExESTBNQ3d5TVRZc01Ua3hMRGMyTERNeExEazRMREUyTml3eE5EQXNOellzTVRBd0xERXlNeXd5TXpVc05qUXNOemdzTVRrekxESXhNaXc0T0N3eU5ETXNNVGszOk1qTXhMREkxTkN3eE1UTXNNalVzTVRZMkxERTROeXd4TVRVc05qUXNNVFUwTERnc01USTJMREV3TERFNU5pd3hNRGdzTWpNNUxERTNNeXd4Tmpnc01qRXNNVGd5TERFMU9RPT06TVRZd0xESTRMREUzTERFNU9Dd3lNaklzTWpNMExERTBOQ3c1TXl3ek55d3hPREFzTVRNMUxERXdOU3d4TkRNc01UY3NOalFzTWpJMExERTVOeXcxTVN3eE5UQXNNakF3Ok1UQXdNREE9Ok1UQTNOVEU0TkRjeU53PT0=:cHJhZ21hIGNhc2hzY3JpcHQgXjAuNi4xOwogICAgICAgICAgICBjb250cmFjdCBlc2Nyb3coYnl0ZXMyMCBzZWxsZXJQa2gsIGJ5dGVzMjAgYnV5ZXJQa2gsIGJ5dGVzMjAgYXJiaXRlclBraCwgaW50IGNvbnRyYWN0QW1vdW50LCBpbnQgY29udHJhY3ROb25jZSkgewoKICAgICAgICAgICAgICAgIGZ1bmN0aW9uIHNwZW5kKHB1YmtleSBzaWduaW5nUGssIHNpZyBzLCBpbnQgYW1vdW50LCBpbnQgbm9uY2UpIHsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBhcmJpdGVyUGtoIHx8IGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBidXllclBraCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShjaGVja1NpZyhzLCBzaWduaW5nUGspKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGFtb3VudCA+PSBjb250cmFjdEFtb3VudCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShub25jZSA9PSBjb250cmFjdE5vbmNlKTsKICAgICAgICAgICAgICAgICAgICBieXRlczM0IG91dHB1dCA9IG5ldyBPdXRwdXRQMlBLSChieXRlczgoYW1vdW50KSwgc2VsbGVyUGtoKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gyNTYob3V0cHV0KSA9PSB0eC5oYXNoT3V0cHV0cyk7CiAgICAgICAgICAgICAgICB9CgogICAgICAgICAgICAgICAgZnVuY3Rpb24gcmVmdW5kKHB1YmtleSBzaWduaW5nUGssIHNpZyBzLCBpbnQgYW1vdW50LCBpbnQgbm9uY2UpIHsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGhhc2gxNjAoc2lnbmluZ1BrKSA9PSBhcmJpdGVyUGtofHxoYXNoMTYwKHNpZ25pbmdQaykgPT0gc2VsbGVyUGtoKTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKGNoZWNrU2lnKHMsIHNpZ25pbmdQaykpOwogICAgICAgICAgICAgICAgICAgIHJlcXVpcmUoYW1vdW50ID49IGNvbnRyYWN0QW1vdW50KTsKICAgICAgICAgICAgICAgICAgICByZXF1aXJlKG5vbmNlID09IGNvbnRyYWN0Tm9uY2UpOwogICAgICAgICAgICAgICAgICAgIGJ5dGVzMzQgb3V0cHV0ID0gbmV3IE91dHB1dFAyUEtIKGJ5dGVzOChhbW91bnQpLCBidXllclBraCk7CiAgICAgICAgICAgICAgICAgICAgcmVxdWlyZShoYXNoMjU2KG91dHB1dCkgPT0gdHguaGFzaE91dHB1dHMpOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9CiAgICAgICAg:1075184727"} # EscrowInfoRequest | Request parsed information regarding a contract from the escrowContractId

    try:
        # Get information about an escrow contract from the escrowContractId
        api_response = api_instance.escrow_info(escrow_info_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractEscrowApi->escrow_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escrow_info_request** | [**EscrowInfoRequest**](EscrowInfoRequest.md)| Request parsed information regarding a contract from the escrowContractId | 

### Return type

[**EscrowInfoResponse**](EscrowInfoResponse.md)

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

# **escrow_utxos**
> UtxoResponse escrow_utxos(escrow_contract)

List specific utxos on any escrow contract

Returns all UTXOs that can be spent by the contract. Both confirmed and unconfirmed UTXOs are included. The endpoint works with contracts generated from templates (i.e. escrow). 

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
    api_instance = mainnet.ContractEscrowApi(api_client)
    escrow_contract = mainnet.EscrowContract() # EscrowContract | 

    try:
        # List specific utxos on any escrow contract
        api_response = api_instance.escrow_utxos(escrow_contract)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContractEscrowApi->escrow_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escrow_contract** | [**EscrowContract**](EscrowContract.md)|  | 

### Return type

[**UtxoResponse**](UtxoResponse.md)

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

