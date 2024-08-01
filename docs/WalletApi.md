# mainnet.WalletApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](WalletApi.md#balance) | **POST** /wallet/balance | Get total balance for wallet
[**create_wallet**](WalletApi.md#create_wallet) | **POST** /wallet/create | create a new wallet
[**deposit_address**](WalletApi.md#deposit_address) | **POST** /wallet/deposit_address | Get a deposit address in cash address format
[**deposit_qr**](WalletApi.md#deposit_qr) | **POST** /wallet/deposit_qr | Get receiving cash address as a qrcode
[**encode_transaction**](WalletApi.md#encode_transaction) | **POST** /wallet/encode_transaction | Encode and sign a transaction given a list of sendRequests, options and estimate fees
[**get_all_nft_token_balances**](WalletApi.md#get_all_nft_token_balances) | **POST** /wallet/get_all_nft_token_balances | Get non-fungible token balance
[**get_all_token_balances**](WalletApi.md#get_all_token_balances) | **POST** /wallet/get_all_token_balances | Get non-fungible token balance
[**get_history**](WalletApi.md#get_history) | **POST** /wallet/get_history | Get a list of transactions related to a wallet
[**get_nft_token_balance**](WalletApi.md#get_nft_token_balance) | **POST** /wallet/get_nft_token_balance | Get non-fungible token balance
[**get_token_balance**](WalletApi.md#get_token_balance) | **POST** /wallet/get_token_balance | Get fungible token balance
[**get_token_utxos**](WalletApi.md#get_token_utxos) | **POST** /wallet/get_token_utxos | Get token utxos
[**info**](WalletApi.md#info) | **POST** /wallet/info | Get information about a wallet
[**max_amount_to_send**](WalletApi.md#max_amount_to_send) | **POST** /wallet/max_amount_to_send | Get maximum spendable amount
[**named_exists**](WalletApi.md#named_exists) | **POST** /wallet/named_exists | Check if a named wallet already exists
[**replace_named**](WalletApi.md#replace_named) | **POST** /wallet/replace_named | Replace (recover) named wallet with a new walletId. If wallet with a provided name does not exist yet, it will be creted with a &#x60;walletId&#x60; supplied If wallet exists it will be overwritten without exception 
[**send**](WalletApi.md#send) | **POST** /wallet/send | Send some amount to a given address
[**send_max**](WalletApi.md#send_max) | **POST** /wallet/send_max | Send all available funds to a given address
[**submit_transaction**](WalletApi.md#submit_transaction) | **POST** /wallet/submit_transaction | submit an encoded and signed transaction to the network
[**token_burn**](WalletApi.md#token_burn) | **POST** /wallet/token_burn | Perform an explicit token burn
[**token_deposit_address**](WalletApi.md#token_deposit_address) | **POST** /wallet/token_deposit_address | Get a token aware deposit address in cash address format
[**token_deposit_qr**](WalletApi.md#token_deposit_qr) | **POST** /wallet/token_deposit_qr | Get receiving token aware cash address as a qrcode
[**token_genesis**](WalletApi.md#token_genesis) | **POST** /wallet/token_genesis | Create new token category
[**token_mint**](WalletApi.md#token_mint) | **POST** /wallet/token_mint | Mint new non-fungible tokens
[**utxos**](WalletApi.md#utxos) | **POST** /wallet/utxo | Get detailed information about unspent outputs (utxos)
[**xpubkeys**](WalletApi.md#xpubkeys) | **POST** /wallet/xpubkeys | A set of xpubkeys and paths for the wallet.


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

# **encode_transaction**
> EncodeTransactionResponse encode_transaction(encode_transaction_request)

Encode and sign a transaction given a list of sendRequests, options and estimate fees

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
    encode_transaction_request = mainnet.EncodeTransactionRequest() # EncodeTransactionRequest | encode a transaction

    try:
        # Encode and sign a transaction given a list of sendRequests, options and estimate fees
        api_response = api_instance.encode_transaction(encode_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->encode_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encode_transaction_request** | [**EncodeTransactionRequest**](EncodeTransactionRequest.md)| encode a transaction | 

### Return type

[**EncodeTransactionResponse**](EncodeTransactionResponse.md)

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

# **get_all_nft_token_balances**
> dict(str, float) get_all_nft_token_balances(inline_object4)

Get non-fungible token balance

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
    inline_object4 = mainnet.InlineObject4() # InlineObject4 | 

    try:
        # Get non-fungible token balance
        api_response = api_instance.get_all_nft_token_balances(inline_object4)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_all_nft_token_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

**dict(str, float)**

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

# **get_all_token_balances**
> dict(str, float) get_all_token_balances(inline_object3)

Get non-fungible token balance

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
    inline_object3 = mainnet.InlineObject3() # InlineObject3 | 

    try:
        # Get non-fungible token balance
        api_response = api_instance.get_all_token_balances(inline_object3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_all_token_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

**dict(str, float)**

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

# **get_history**
> list[TransactionHistoryItem] get_history(history_request)

Get a list of transactions related to a wallet

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
    history_request = mainnet.HistoryRequest() # HistoryRequest | Gets transaction history of this wallet with most data decoded and ready to present to user   Note: balance calculations are valid only if querying to the blockchain tip (`toHeight` === -1, `count` === -1)   Note: this method is heavy on network calls, if invoked in browser use of cache is advised, @see `Config.UseLocalStorageCache`   Note: this method tries to recreate the history tab view of Electron Cash wallet, however, it may not be 100% accurate if the tnransaction value changes are the same in the same block (ordering) 

    try:
        # Get a list of transactions related to a wallet
        api_response = api_instance.get_history(history_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history_request** | [**HistoryRequest**](HistoryRequest.md)| Gets transaction history of this wallet with most data decoded and ready to present to user   Note: balance calculations are valid only if querying to the blockchain tip (&#x60;toHeight&#x60; &#x3D;&#x3D;&#x3D; -1, &#x60;count&#x60; &#x3D;&#x3D;&#x3D; -1)   Note: this method is heavy on network calls, if invoked in browser use of cache is advised, @see &#x60;Config.UseLocalStorageCache&#x60;   Note: this method tries to recreate the history tab view of Electron Cash wallet, however, it may not be 100% accurate if the tnransaction value changes are the same in the same block (ordering)  | 

### Return type

[**list[TransactionHistoryItem]**](TransactionHistoryItem.md)

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

# **get_nft_token_balance**
> object get_nft_token_balance(inline_object2)

Get non-fungible token balance

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
    inline_object2 = mainnet.InlineObject2() # InlineObject2 | 

    try:
        # Get non-fungible token balance
        api_response = api_instance.get_nft_token_balance(inline_object2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_nft_token_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

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

# **get_token_balance**
> object get_token_balance(inline_object1)

Get fungible token balance

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
    inline_object1 = mainnet.InlineObject1() # InlineObject1 | 

    try:
        # Get fungible token balance
        api_response = api_instance.get_token_balance(inline_object1)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_token_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

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

# **get_token_utxos**
> list[Utxo] get_token_utxos(inline_object)

Get token utxos

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
    inline_object = mainnet.InlineObject() # InlineObject | 

    try:
        # Get token utxos
        api_response = api_instance.get_token_utxos(inline_object)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->get_token_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**list[Utxo]**](Utxo.md)

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

# **submit_transaction**
> SubmitTransactionResponse submit_transaction(submit_transaction_request)

submit an encoded and signed transaction to the network

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
    submit_transaction_request = mainnet.SubmitTransactionRequest() # SubmitTransactionRequest | submit an encoded and signed transaction to the network

    try:
        # submit an encoded and signed transaction to the network
        api_response = api_instance.submit_transaction(submit_transaction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->submit_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_transaction_request** | [**SubmitTransactionRequest**](SubmitTransactionRequest.md)| submit an encoded and signed transaction to the network | 

### Return type

[**SubmitTransactionResponse**](SubmitTransactionResponse.md)

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

# **token_burn**
> SendResponse token_burn(token_burn_request)

Perform an explicit token burn

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
    token_burn_request = mainnet.TokenBurnRequest() # TokenBurnRequest | Perform an explicit token burning by spending a token utxo to an OP_RETURN Behaves differently for fungible and non-fungible tokens:  * NFTs are always \"destroyed\"  * FTs' amount is reduced by the amount specified, if 0 FT amount is left and no NFT present, the token is \"destroyed\" Refer to spec https://github.com/bitjson/cashtokens 

    try:
        # Perform an explicit token burn
        api_response = api_instance.token_burn(token_burn_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->token_burn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_burn_request** | [**TokenBurnRequest**](TokenBurnRequest.md)| Perform an explicit token burning by spending a token utxo to an OP_RETURN Behaves differently for fungible and non-fungible tokens:  * NFTs are always \&quot;destroyed\&quot;  * FTs&#39; amount is reduced by the amount specified, if 0 FT amount is left and no NFT present, the token is \&quot;destroyed\&quot; Refer to spec https://github.com/bitjson/cashtokens  | 

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
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_deposit_address**
> DepositAddressResponse token_deposit_address(serialized_wallet)

Get a token aware deposit address in cash address format

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
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a token aware deposit address given a wallet 

    try:
        # Get a token aware deposit address in cash address format
        api_response = api_instance.token_deposit_address(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->token_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a token aware deposit address given a wallet  | 

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

# **token_deposit_qr**
> ScalableVectorGraphic token_deposit_qr(serialized_wallet)

Get receiving token aware cash address as a qrcode

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
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a token aware deposit cash address as a Quick Response code (qrcode) 

    try:
        # Get receiving token aware cash address as a qrcode
        api_response = api_instance.token_deposit_qr(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->token_deposit_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a token aware deposit cash address as a Quick Response code (qrcode)  | 

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

# **token_genesis**
> SendResponse token_genesis(token_genesis_request)

Create new token category

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
    token_genesis_request = mainnet.TokenGenesisRequest() # TokenGenesisRequest | Create new cashtoken, both funglible and/or non-fungible (NFT) Refer to spec https://github.com/bitjson/cashtokens Newly created token identifier can be found in `tokenIds` field. 

    try:
        # Create new token category
        api_response = api_instance.token_genesis(token_genesis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->token_genesis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_genesis_request** | [**TokenGenesisRequest**](TokenGenesisRequest.md)| Create new cashtoken, both funglible and/or non-fungible (NFT) Refer to spec https://github.com/bitjson/cashtokens Newly created token identifier can be found in &#x60;tokenIds&#x60; field.  | 

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
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_mint**
> SendResponse token_mint(token_mint_request)

Mint new non-fungible tokens

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
    token_mint_request = mainnet.TokenMintRequest() # TokenMintRequest | Mint new NFT cashtokens using an existing minting token Refer to spec https://github.com/bitjson/cashtokens Newly minted tokens will retain the parent's `tokenId`. 

    try:
        # Mint new non-fungible tokens
        api_response = api_instance.token_mint(token_mint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->token_mint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_mint_request** | [**TokenMintRequest**](TokenMintRequest.md)| Mint new NFT cashtokens using an existing minting token Refer to spec https://github.com/bitjson/cashtokens Newly minted tokens will retain the parent&#39;s &#x60;tokenId&#x60;.  | 

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
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **utxos**
> list[Utxo] utxos(serialized_wallet)

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

[**list[Utxo]**](Utxo.md)

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

# **xpubkeys**
> XPubKeyResponse xpubkeys(x_pub_key_request)

A set of xpubkeys and paths for the wallet.

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
    x_pub_key_request = mainnet.XPubKeyRequest() # XPubKeyRequest | x 

    try:
        # A set of xpubkeys and paths for the wallet.
        api_response = api_instance.xpubkeys(x_pub_key_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletApi->xpubkeys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_pub_key_request** | [**XPubKeyRequest**](XPubKeyRequest.md)| x  | 

### Return type

[**XPubKeyResponse**](XPubKeyResponse.md)

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

