# mainnet.WebhookApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_address**](WebhookApi.md#watch_address) | **POST** /webhook/watch_address | Create a webhook to watch cashaddress balance and transactions. 


# **watch_address**
> WatchAddressResponse watch_address(watch_address_request)

Create a webhook to watch cashaddress balance and transactions. 

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
    api_instance = mainnet.WebhookApi(api_client)
    watch_address_request = mainnet.WatchAddressRequest() # WatchAddressRequest | Based on the 'type' parameter the webhook will be triggered to either post balance or raw transactions to the 'url': - 'transaction:in' for incoming BCH transactions - 'transaction:out' for outgoing BCH transactions - 'transaction:in,out' both for incoming and outgoing BCH transactions - 'balance' will post the object according to 'BalanceResponse' schema 

    try:
        # Create a webhook to watch cashaddress balance and transactions. 
        api_response = api_instance.watch_address(watch_address_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebhookApi->watch_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch_address_request** | [**WatchAddressRequest**](WatchAddressRequest.md)| Based on the &#39;type&#39; parameter the webhook will be triggered to either post balance or raw transactions to the &#39;url&#39;: - &#39;transaction:in&#39; for incoming BCH transactions - &#39;transaction:out&#39; for outgoing BCH transactions - &#39;transaction:in,out&#39; both for incoming and outgoing BCH transactions - &#39;balance&#39; will post the object according to &#39;BalanceResponse&#39; schema  | 

### Return type

[**WatchAddressResponse**](WatchAddressResponse.md)

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

