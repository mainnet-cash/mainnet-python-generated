# mainnet.WalletUtilApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**util_decode_transaction**](WalletUtilApi.md#util_decode_transaction) | **POST** /wallet/util/decode_transaction | Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.


# **util_decode_transaction**
> ElectrumRawTransaction util_decode_transaction(util_decode_transaction_request)

Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.

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
    api_instance = mainnet.WalletUtilApi(api_client)
    util_decode_transaction_request = mainnet.UtilDecodeTransactionRequest() # UtilDecodeTransactionRequest | Request to decode a transaction 

    try:
        # Decode a bitcoin transaction. Accepts both transaction hash or raw transaction in hex format.
        api_response = api_instance.util_decode_transaction(util_decode_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletUtilApi->util_decode_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **util_decode_transaction_request** | [**UtilDecodeTransactionRequest**](UtilDecodeTransactionRequest.md)| Request to decode a transaction  | 

### Return type

[**ElectrumRawTransaction**](ElectrumRawTransaction.md)

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

