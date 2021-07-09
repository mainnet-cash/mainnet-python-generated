# mainnet.WalletSlpApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nft_child_genesis**](WalletSlpApi.md#nft_child_genesis) | **POST** /wallet/slp/nft_child_genesis | Get created tokenId back and new NFT child token balance of the wallet
[**nft_parent_genesis**](WalletSlpApi.md#nft_parent_genesis) | **POST** /wallet/slp/nft_parent_genesis | Get created tokenId back and new NFT token balance of the wallet
[**slp_all_balances**](WalletSlpApi.md#slp_all_balances) | **POST** /wallet/slp/all_balances | Get all slp balances of the wallet
[**slp_balance**](WalletSlpApi.md#slp_balance) | **POST** /wallet/slp/balance | Get total slp token balance of the wallet
[**slp_create_wallet**](WalletSlpApi.md#slp_create_wallet) | **POST** /wallet/slp/create | create a new SLP wallet
[**slp_deposit_address**](WalletSlpApi.md#slp_deposit_address) | **POST** /wallet/slp/deposit_address | Get an SLP deposit address in cash address format
[**slp_deposit_qr**](WalletSlpApi.md#slp_deposit_qr) | **POST** /wallet/slp/deposit_qr | Get an SLP receiving cash address as a qrcode
[**slp_genesis**](WalletSlpApi.md#slp_genesis) | **POST** /wallet/slp/genesis | Get created tokenId back and new slp token balance of the wallet
[**slp_mint**](WalletSlpApi.md#slp_mint) | **POST** /wallet/slp/mint | Get created tokenId back and new slp token balance of the wallet
[**slp_outpoints**](WalletSlpApi.md#slp_outpoints) | **POST** /wallet/slp/outpoints | Get list of unspent SLP outpoints.
[**slp_send**](WalletSlpApi.md#slp_send) | **POST** /wallet/slp/send | Send some SLP token amount to a given cash address
[**slp_send_max**](WalletSlpApi.md#slp_send_max) | **POST** /wallet/slp/send_max | Send all available SLP funds to a given address
[**slp_token_info**](WalletSlpApi.md#slp_token_info) | **POST** /wallet/slp/token_info | Get information about the token
[**slp_utxos**](WalletSlpApi.md#slp_utxos) | **POST** /wallet/slp/utxo | Get detailed information about unspent SLP outputs (utxos)


# **nft_child_genesis**
> SlpGenesisResponse nft_child_genesis(slp_genesis_request)

Get created tokenId back and new NFT child token balance of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_genesis_request = mainnet.SlpGenesisRequest() # SlpGenesisRequest | Request to create a new NFT child token (genesis) by consuming a parent token 

    try:
        # Get created tokenId back and new NFT child token balance of the wallet
        api_response = api_instance.nft_child_genesis(slp_genesis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->nft_child_genesis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_genesis_request** | [**SlpGenesisRequest**](SlpGenesisRequest.md)| Request to create a new NFT child token (genesis) by consuming a parent token  | 

### Return type

[**SlpGenesisResponse**](SlpGenesisResponse.md)

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

# **nft_parent_genesis**
> SlpGenesisResponse nft_parent_genesis(slp_genesis_request)

Get created tokenId back and new NFT token balance of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_genesis_request = mainnet.SlpGenesisRequest() # SlpGenesisRequest | Request to create a new NFT parent token (genesis) 

    try:
        # Get created tokenId back and new NFT token balance of the wallet
        api_response = api_instance.nft_parent_genesis(slp_genesis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->nft_parent_genesis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_genesis_request** | [**SlpGenesisRequest**](SlpGenesisRequest.md)| Request to create a new NFT parent token (genesis)  | 

### Return type

[**SlpGenesisResponse**](SlpGenesisResponse.md)

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

# **slp_all_balances**
> list[SlpBalanceResponse] slp_all_balances(serialized_wallet)

Get all slp balances of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a wallet slp balances 

    try:
        # Get all slp balances of the wallet
        api_response = api_instance.slp_all_balances(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_all_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a wallet slp balances  | 

### Return type

[**list[SlpBalanceResponse]**](SlpBalanceResponse.md)

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

# **slp_balance**
> SlpBalanceResponse slp_balance(slp_balance_request)

Get total slp token balance of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_balance_request = mainnet.SlpBalanceRequest() # SlpBalanceRequest | Request for a wallet slp token balance 

    try:
        # Get total slp token balance of the wallet
        api_response = api_instance.slp_balance(slp_balance_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_balance_request** | [**SlpBalanceRequest**](SlpBalanceRequest.md)| Request for a wallet slp token balance  | 

### Return type

[**SlpBalanceResponse**](SlpBalanceResponse.md)

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

# **slp_create_wallet**
> WalletResponse slp_create_wallet(wallet_request)

create a new SLP wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    wallet_request = mainnet.WalletRequest() # WalletRequest | Request a new SLP wallet

    try:
        # create a new SLP wallet
        api_response = api_instance.slp_create_wallet(wallet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_create_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_request** | [**WalletRequest**](WalletRequest.md)| Request a new SLP wallet | 

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

# **slp_deposit_address**
> SlpDepositAddressResponse slp_deposit_address(serialized_wallet)

Get an SLP deposit address in cash address format

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
    api_instance = mainnet.WalletSlpApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for an SLP deposit address given a wallet 

    try:
        # Get an SLP deposit address in cash address format
        api_response = api_instance.slp_deposit_address(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for an SLP deposit address given a wallet  | 

### Return type

[**SlpDepositAddressResponse**](SlpDepositAddressResponse.md)

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

# **slp_deposit_qr**
> ScalableVectorGraphic slp_deposit_qr(serialized_wallet)

Get an SLP receiving cash address as a qrcode

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
    api_instance = mainnet.WalletSlpApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for an SLP deposit cash address as a Quick Response code (qrcode) 

    try:
        # Get an SLP receiving cash address as a qrcode
        api_response = api_instance.slp_deposit_qr(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_deposit_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for an SLP deposit cash address as a Quick Response code (qrcode)  | 

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

# **slp_genesis**
> SlpGenesisResponse slp_genesis(slp_genesis_request)

Get created tokenId back and new slp token balance of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_genesis_request = mainnet.SlpGenesisRequest() # SlpGenesisRequest | Request to create a new SLP token (genesis) 

    try:
        # Get created tokenId back and new slp token balance of the wallet
        api_response = api_instance.slp_genesis(slp_genesis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_genesis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_genesis_request** | [**SlpGenesisRequest**](SlpGenesisRequest.md)| Request to create a new SLP token (genesis)  | 

### Return type

[**SlpGenesisResponse**](SlpGenesisResponse.md)

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

# **slp_mint**
> SlpMintResponse slp_mint(slp_mint_request)

Get created tokenId back and new slp token balance of the wallet

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_mint_request = mainnet.SlpMintRequest() # SlpMintRequest | Request to mint more of SLP tokens 

    try:
        # Get created tokenId back and new slp token balance of the wallet
        api_response = api_instance.slp_mint(slp_mint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_mint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_mint_request** | [**SlpMintRequest**](SlpMintRequest.md)| Request to mint more of SLP tokens  | 

### Return type

[**SlpMintResponse**](SlpMintResponse.md)

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

# **slp_outpoints**
> SlpOutpointsResponse slp_outpoints(serialized_wallet)

Get list of unspent SLP outpoints.

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
    api_instance = mainnet.WalletSlpApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request of unspent SLP outpoints 

    try:
        # Get list of unspent SLP outpoints.
        api_response = api_instance.slp_outpoints(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_outpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request of unspent SLP outpoints  | 

### Return type

[**SlpOutpointsResponse**](SlpOutpointsResponse.md)

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

# **slp_send**
> SlpSendResponse slp_send(slp_send_request)

Send some SLP token amount to a given cash address

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_send_request = mainnet.SlpSendRequest() # SlpSendRequest | place an SLP send request

    try:
        # Send some SLP token amount to a given cash address
        api_response = api_instance.slp_send(slp_send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_send_request** | [**SlpSendRequest**](SlpSendRequest.md)| place an SLP send request | 

### Return type

[**SlpSendResponse**](SlpSendResponse.md)

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

# **slp_send_max**
> SlpSendResponse slp_send_max(slp_send_max_request)

Send all available SLP funds to a given address

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_send_max_request = mainnet.SlpSendMaxRequest() # SlpSendMaxRequest | Request to send all available SLP funds to a given address

    try:
        # Send all available SLP funds to a given address
        api_response = api_instance.slp_send_max(slp_send_max_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_send_max: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_send_max_request** | [**SlpSendMaxRequest**](SlpSendMaxRequest.md)| Request to send all available SLP funds to a given address | 

### Return type

[**SlpSendResponse**](SlpSendResponse.md)

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

# **slp_token_info**
> SlpTokenInfoResponse slp_token_info(slp_token_info_request)

Get information about the token

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
    api_instance = mainnet.WalletSlpApi(api_client)
    slp_token_info_request = mainnet.SlpTokenInfoRequest() # SlpTokenInfoRequest | Request to get information about the token 

    try:
        # Get information about the token
        api_response = api_instance.slp_token_info(slp_token_info_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_token_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slp_token_info_request** | [**SlpTokenInfoRequest**](SlpTokenInfoRequest.md)| Request to get information about the token  | 

### Return type

[**SlpTokenInfoResponse**](SlpTokenInfoResponse.md)

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

# **slp_utxos**
> SlpUtxoResponse slp_utxos(serialized_wallet)

Get detailed information about unspent SLP outputs (utxos)

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
    api_instance = mainnet.WalletSlpApi(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request detailed list of unspent SLP transaction outputs 

    try:
        # Get detailed information about unspent SLP outputs (utxos)
        api_response = api_instance.slp_utxos(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WalletSlpApi->slp_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request detailed list of unspent SLP transaction outputs  | 

### Return type

[**SlpUtxoResponse**](SlpUtxoResponse.md)

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

