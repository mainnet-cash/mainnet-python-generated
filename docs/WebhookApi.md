# mainnet.WebhookApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_address**](WebhookApi.md#watch_address) | **POST** /webhook/watch_address | Create a webhook to watch cashaddress balance and transactions. 


# **watch_address**
> WatchAddressResponse watch_address(watch_address_request)

Create a webhook to watch cashaddress balance and transactions. 

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
    api_instance = mainnet.WebhookApi(api_client)
    watch_address_request = mainnet.WatchAddressRequest() # WatchAddressRequest | Based on the 'type' parameter the webhook will be triggered to either post balance or raw transactions to the 'url' - 'transaction:in' for incoming only, 'transaction:out' for outgoing only and 'transaction:in,out' both for incoming and outgoing transactions. 'balance' will post the object according to 'BalanceResponse' schema 

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
 **watch_address_request** | [**WatchAddressRequest**](WatchAddressRequest.md)| Based on the &#39;type&#39; parameter the webhook will be triggered to either post balance or raw transactions to the &#39;url&#39; - &#39;transaction:in&#39; for incoming only, &#39;transaction:out&#39; for outgoing only and &#39;transaction:in,out&#39; both for incoming and outgoing transactions. &#39;balance&#39; will post the object according to &#39;BalanceResponse&#39; schema  | 

### Return type

[**WatchAddressResponse**](WatchAddressResponse.md)

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

