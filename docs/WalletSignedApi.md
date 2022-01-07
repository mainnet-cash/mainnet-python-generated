# mainnet.WalletSignedApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signed_message_sign**](WalletSignedApi.md#signed_message_sign) | **POST** /wallet/signed/sign | Returns the message signature
[**signed_message_verify**](WalletSignedApi.md#signed_message_verify) | **POST** /wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address


# **signed_message_sign**
> SignedMessageResponse signed_message_sign(create_signed_message_request=create_signed_message_request)

Returns the message signature

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
    api_instance = mainnet.WalletSignedApi(api_client)
    create_signed_message_request = mainnet.CreateSignedMessageRequest() # CreateSignedMessageRequest | Sign a message  (optional)

    try:
        # Returns the message signature
        api_response = api_instance.signed_message_sign(create_signed_message_request=create_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSignedApi->signed_message_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_signed_message_request** | [**CreateSignedMessageRequest**](CreateSignedMessageRequest.md)| Sign a message  | [optional] 

### Return type

[**SignedMessageResponse**](SignedMessageResponse.md)

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

# **signed_message_verify**
> VerifySignedMessageResponse signed_message_verify(verify_signed_message_request=verify_signed_message_request)

Returns a boolean indicating whether message was valid for a given address

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
    api_instance = mainnet.WalletSignedApi(api_client)
    verify_signed_message_request = mainnet.VerifySignedMessageRequest() # VerifySignedMessageRequest | Sign a message  (optional)

    try:
        # Returns a boolean indicating whether message was valid for a given address
        api_response = api_instance.signed_message_verify(verify_signed_message_request=verify_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSignedApi->signed_message_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_signed_message_request** | [**VerifySignedMessageRequest**](VerifySignedMessageRequest.md)| Sign a message  | [optional] 

### Return type

[**VerifySignedMessageResponse**](VerifySignedMessageResponse.md)

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

