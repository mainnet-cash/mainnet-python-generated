# mainnet.SmartbchWalletApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smartbch_balance**](SmartbchWalletApi.md#smartbch_balance) | **POST** /smartbch/wallet/balance | Get total balance for wallet
[**smartbch_create_wallet**](SmartbchWalletApi.md#smartbch_create_wallet) | **POST** /smartbch/wallet/create | create a new wallet
[**smartbch_deposit_address**](SmartbchWalletApi.md#smartbch_deposit_address) | **POST** /smartbch/wallet/deposit_address | Get a deposit address
[**smartbch_deposit_qr**](SmartbchWalletApi.md#smartbch_deposit_qr) | **POST** /smartbch/wallet/deposit_qr | Get receiving cash address as a qrcode
[**smartbch_max_amount_to_send**](SmartbchWalletApi.md#smartbch_max_amount_to_send) | **POST** /smartbch/wallet/max_amount_to_send | Get maximum spendable amount
[**smartbch_send**](SmartbchWalletApi.md#smartbch_send) | **POST** /smartbch/wallet/send | Send some amount to a given address
[**smartbch_send_max**](SmartbchWalletApi.md#smartbch_send_max) | **POST** /smartbch/wallet/send_max | Send all available funds to a given address
[**smartbch_signed_message_sign**](SmartbchWalletApi.md#smartbch_signed_message_sign) | **POST** /smartbch/wallet/signed/sign | Returns the message signature
[**smartbch_signed_message_verify**](SmartbchWalletApi.md#smartbch_signed_message_verify) | **POST** /smartbch/wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address


# **smartbch_balance**
> BalanceResponse smartbch_balance(balance_request)

Get total balance for wallet

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    balance_request = mainnet.BalanceRequest() # BalanceRequest | Request for a wallet balance 

    try:
        # Get total balance for wallet
        api_response = api_instance.smartbch_balance(balance_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_request** | [**BalanceRequest**](BalanceRequest.md)| Request for a wallet balance  | 

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smartbch_create_wallet**
> WalletResponse smartbch_create_wallet(wallet_request)

create a new wallet

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    wallet_request = mainnet.WalletRequest() # WalletRequest | Request a new random wallet

    try:
        # create a new wallet
        api_response = api_instance.smartbch_create_wallet(wallet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_create_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_request** | [**WalletRequest**](WalletRequest.md)| Request a new random wallet | 

### Return type

[**WalletResponse**](WalletResponse.md)

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

# **smartbch_deposit_address**
> SmartBchDepositAddressResponse smartbch_deposit_address(serialized_wallet)

Get a deposit address

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a deposit address given a wallet 

    try:
        # Get a deposit address
        api_response = api_instance.smartbch_deposit_address(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a deposit address given a wallet  | 

### Return type

[**SmartBchDepositAddressResponse**](SmartBchDepositAddressResponse.md)

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

# **smartbch_deposit_qr**
> ScalableVectorGraphic smartbch_deposit_qr(serialized_wallet)

Get receiving cash address as a qrcode

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a deposit cash address as a Quick Response code (qrcode) 

    try:
        # Get receiving cash address as a qrcode
        api_response = api_instance.smartbch_deposit_qr(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_deposit_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a deposit cash address as a Quick Response code (qrcode)  | 

### Return type

[**ScalableVectorGraphic**](ScalableVectorGraphic.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Qr code image data encoded string in the src field suitable for inclusion in html using:    - \\&lt;img src\\&#x3D;\\\&quot;{response.src}\&quot;\\&gt;  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smartbch_max_amount_to_send**
> BalanceResponse smartbch_max_amount_to_send(smart_bch_max_amount_to_send_request)

Get maximum spendable amount

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    smart_bch_max_amount_to_send_request = mainnet.SmartBchMaxAmountToSendRequest() # SmartBchMaxAmountToSendRequest | get amount that will be spend with a spend max request. If a unit type is specified, a numeric value will be returned.

    try:
        # Get maximum spendable amount
        api_response = api_instance.smartbch_max_amount_to_send(smart_bch_max_amount_to_send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_max_amount_to_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_max_amount_to_send_request** | [**SmartBchMaxAmountToSendRequest**](SmartBchMaxAmountToSendRequest.md)| get amount that will be spend with a spend max request. If a unit type is specified, a numeric value will be returned. | 

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | transaction accepted |  -  |
**400** | Invalid Request |  -  |
**418** | Invalid network for given address |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smartbch_send**
> list[SmartBchSendResponseItem] smartbch_send(smart_bch_send_request)

Send some amount to a given address

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    smart_bch_send_request = mainnet.SmartBchSendRequest() # SmartBchSendRequest | place a send request

    try:
        # Send some amount to a given address
        api_response = api_instance.smartbch_send(smart_bch_send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_send_request** | [**SmartBchSendRequest**](SmartBchSendRequest.md)| place a send request | 

### Return type

[**list[SmartBchSendResponseItem]**](SmartBchSendResponseItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | transaction accepted |  -  |
**400** | Invalid Request |  -  |
**418** | Invalid network for given address |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smartbch_send_max**
> SmartBchSendResponseItem smartbch_send_max(smart_bch_send_max_request)

Send all available funds to a given address

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    smart_bch_send_max_request = mainnet.SmartBchSendMaxRequest() # SmartBchSendMaxRequest | Request to send all available funds to a given address

    try:
        # Send all available funds to a given address
        api_response = api_instance.smartbch_send_max(smart_bch_send_max_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_send_max: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_send_max_request** | [**SmartBchSendMaxRequest**](SmartBchSendMaxRequest.md)| Request to send all available funds to a given address | 

### Return type

[**SmartBchSendResponseItem**](SmartBchSendResponseItem.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | transaction accepted |  -  |
**400** | Invalid Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smartbch_signed_message_sign**
> SignedMessageResponse smartbch_signed_message_sign(create_signed_message_request=create_signed_message_request)

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    create_signed_message_request = mainnet.CreateSignedMessageRequest() # CreateSignedMessageRequest | Sign a message  (optional)

    try:
        # Returns the message signature
        api_response = api_instance.smartbch_signed_message_sign(create_signed_message_request=create_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_signed_message_sign: %s\n" % e)
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

# **smartbch_signed_message_verify**
> VerifySignedMessageResponse smartbch_signed_message_verify(verify_signed_message_request=verify_signed_message_request)

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
    api_instance = mainnet.SmartbchWalletApi(api_client)
    verify_signed_message_request = mainnet.VerifySignedMessageRequest() # VerifySignedMessageRequest | Sign a message  (optional)

    try:
        # Returns a boolean indicating whether message was valid for a given address
        api_response = api_instance.smartbch_signed_message_verify(verify_signed_message_request=verify_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchWalletApi->smartbch_signed_message_verify: %s\n" % e)
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

