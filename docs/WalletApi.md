# mainnet.WalletApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](WalletApi.md#balance) | **POST** /wallet/balance | Get total balance for wallet
[**create_wallet**](WalletApi.md#create_wallet) | **POST** /wallet/create | create a new wallet
[**deposit_address**](WalletApi.md#deposit_address) | **POST** /wallet/deposit_address | Get a deposit address in cash address format
[**deposit_qr**](WalletApi.md#deposit_qr) | **POST** /wallet/deposit_qr | Get receiving cash address as a qrcode
[**info**](WalletApi.md#info) | **POST** /wallet/info | Get information about a wallet
[**max_amount_to_send**](WalletApi.md#max_amount_to_send) | **POST** /wallet/max_amount_to_send | Get maximum spendable amount
[**named_exists**](WalletApi.md#named_exists) | **POST** /wallet/named_exists | Check if a named wallet already exists
[**replace_named**](WalletApi.md#replace_named) | **POST** /wallet/replace_named | Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a &#x60;walletId&#x60; supplied If wallet exists it will be overwritten without exception 
[**send**](WalletApi.md#send) | **POST** /wallet/send | Send some amount to a given address
[**send_max**](WalletApi.md#send_max) | **POST** /wallet/send_max | Send all available funds to a given address
[**signed_message_sign**](WalletApi.md#signed_message_sign) | **POST** /wallet/signed/sign | Returns the message signature
[**signed_message_verify**](WalletApi.md#signed_message_verify) | **POST** /wallet/signed/verify | Returns a boolean indicating whether message was valid for a given address
[**utxos**](WalletApi.md#utxos) | **POST** /wallet/utxo | Get detailed information about unspent outputs (utxos)


# **balance**
> BalanceResponse balance(balance_request)

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
    api_instance = mainnet.WalletApi(api_client)
    balance_request = mainnet.BalanceRequest() # BalanceRequest | Request for a wallet balance 

    try:
        # Get total balance for wallet
        api_response = api_instance.balance(balance_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->balance: %s\n" % e)
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

# **create_wallet**
> WalletResponse create_wallet(wallet_request)

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
    api_instance = mainnet.WalletApi(api_client)
    wallet_request = mainnet.WalletRequest() # WalletRequest | Request a new random wallet

    try:
        # create a new wallet
        api_response = api_instance.create_wallet(wallet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->create_wallet: %s\n" % e)
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

# **deposit_address**
> DepositAddressResponse deposit_address(serialized_wallet)

Get a deposit address in cash address format

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
    api_instance = mainnet.WalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a deposit address given a wallet 

    try:
        # Get a deposit address in cash address format
        api_response = api_instance.deposit_address(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a deposit address given a wallet  | 

### Return type

[**DepositAddressResponse**](DepositAddressResponse.md)

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

# **deposit_qr**
> ScalableVectorGraphic deposit_qr(serialized_wallet)

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
    api_instance = mainnet.WalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a deposit cash address as a Quick Response code (qrcode) 

    try:
        # Get receiving cash address as a qrcode
        api_response = api_instance.deposit_qr(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->deposit_qr: %s\n" % e)
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

# **info**
> WalletInfo info(serialized_wallet)

Get information about a wallet

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
    api_instance = mainnet.WalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | The wallet to request information about, in serialized form. 

    try:
        # Get information about a wallet
        api_response = api_instance.info(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| The wallet to request information about, in serialized form.  | 

### Return type

[**WalletInfo**](WalletInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information about the wallet network, type, and keys  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **max_amount_to_send**
> BalanceResponse max_amount_to_send(max_amount_to_send_request)

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
    api_instance = mainnet.WalletApi(api_client)
    max_amount_to_send_request = mainnet.MaxAmountToSendRequest() # MaxAmountToSendRequest | get amount that will be spend with a spend max request. If a unit type is specified, a numeric value will be returned.

    try:
        # Get maximum spendable amount
        api_response = api_instance.max_amount_to_send(max_amount_to_send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->max_amount_to_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_amount_to_send_request** | [**MaxAmountToSendRequest**](MaxAmountToSendRequest.md)| get amount that will be spend with a spend max request. If a unit type is specified, a numeric value will be returned. | 

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

# **named_exists**
> bool named_exists(wallet_named_exists_request)

Check if a named wallet already exists

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
    api_instance = mainnet.WalletApi(api_client)
    wallet_named_exists_request = mainnet.WalletNamedExistsRequest() # WalletNamedExistsRequest | Request parameters

    try:
        # Check if a named wallet already exists
        api_response = api_instance.named_exists(wallet_named_exists_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->named_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_named_exists_request** | [**WalletNamedExistsRequest**](WalletNamedExistsRequest.md)| Request parameters | 

### Return type

**bool**

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

# **replace_named**
> bool replace_named(wallet_replace_named_request)

Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a `walletId` supplied If wallet exists it will be overwritten without exception 

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
    api_instance = mainnet.WalletApi(api_client)
    wallet_replace_named_request = mainnet.WalletReplaceNamedRequest() # WalletReplaceNamedRequest | Request parameters

    try:
        # Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a `walletId` supplied If wallet exists it will be overwritten without exception 
        api_response = api_instance.replace_named(wallet_replace_named_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->replace_named: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_replace_named_request** | [**WalletReplaceNamedRequest**](WalletReplaceNamedRequest.md)| Request parameters | 

### Return type

**bool**

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

# **send**
> SendResponse send(send_request)

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
    api_instance = mainnet.WalletApi(api_client)
    send_request = mainnet.SendRequest() # SendRequest | place a send request

    try:
        # Send some amount to a given address
        api_response = api_instance.send(send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_request** | [**SendRequest**](SendRequest.md)| place a send request | 

### Return type

[**SendResponse**](SendResponse.md)

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

# **send_max**
> SendMaxResponse send_max(send_max_request)

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
    api_instance = mainnet.WalletApi(api_client)
    send_max_request = mainnet.SendMaxRequest() # SendMaxRequest | Request to send all available funds to a given address

    try:
        # Send all available funds to a given address
        api_response = api_instance.send_max(send_max_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->send_max: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_max_request** | [**SendMaxRequest**](SendMaxRequest.md)| Request to send all available funds to a given address | 

### Return type

[**SendMaxResponse**](SendMaxResponse.md)

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
    api_instance = mainnet.WalletApi(api_client)
    create_signed_message_request = mainnet.CreateSignedMessageRequest() # CreateSignedMessageRequest | Sign a message  (optional)

    try:
        # Returns the message signature
        api_response = api_instance.signed_message_sign(create_signed_message_request=create_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->signed_message_sign: %s\n" % e)
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
    api_instance = mainnet.WalletApi(api_client)
    verify_signed_message_request = mainnet.VerifySignedMessageRequest() # VerifySignedMessageRequest | Sign a message  (optional)

    try:
        # Returns a boolean indicating whether message was valid for a given address
        api_response = api_instance.signed_message_verify(verify_signed_message_request=verify_signed_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->signed_message_verify: %s\n" % e)
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

# **utxos**
> UtxoResponse utxos(serialized_wallet)

Get detailed information about unspent outputs (utxos)

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
    api_instance = mainnet.WalletApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request detailed list of unspent transaction outputs 

    try:
        # Get detailed information about unspent outputs (utxos)
        api_response = api_instance.utxos(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request detailed list of unspent transaction outputs  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

