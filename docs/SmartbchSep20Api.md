# mainnet.SmartbchSep20Api

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_bch_sep20_balance**](SmartbchSep20Api.md#smart_bch_sep20_balance) | **POST** /smartbch/sep20/balance | Get total SmartBch SEP20 token balance of the wallet
[**smart_bch_sep20_deposit_address**](SmartbchSep20Api.md#smart_bch_sep20_deposit_address) | **POST** /smartbch/sep20/deposit_address | Get an SmartBch SEP20 deposit address
[**smart_bch_sep20_deposit_qr**](SmartbchSep20Api.md#smart_bch_sep20_deposit_qr) | **POST** /smartbch/sep20/deposit_qr | Get an SmartBch SEP20 receiving address as a qrcode
[**smart_bch_sep20_genesis**](SmartbchSep20Api.md#smart_bch_sep20_genesis) | **POST** /smartbch/sep20/genesis | Get created tokenId back and new SmartBch SEP20 token balance of the wallet
[**smart_bch_sep20_mint**](SmartbchSep20Api.md#smart_bch_sep20_mint) | **POST** /smartbch/sep20/mint | Get created tokenId back and new SmartBch SEP20 token balance of the wallet
[**smart_bch_sep20_send**](SmartbchSep20Api.md#smart_bch_sep20_send) | **POST** /smartbch/sep20/send | Send some SmartBch SEP20 token amount to a given address
[**smart_bch_sep20_send_max**](SmartbchSep20Api.md#smart_bch_sep20_send_max) | **POST** /smartbch/sep20/send_max | Send all available SmartBch SEP20 token funds to a given address
[**smart_bch_sep20_token_info**](SmartbchSep20Api.md#smart_bch_sep20_token_info) | **POST** /smartbch/sep20/token_info | Get information about the SmartBch SEP20 token


# **smart_bch_sep20_balance**
> SmartBchSep20BalanceResponse smart_bch_sep20_balance(smart_bch_sep20_balance_request)

Get total SmartBch SEP20 token balance of the wallet

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_balance_request = mainnet.SmartBchSep20BalanceRequest() # SmartBchSep20BalanceRequest | Request for a wallet SmartBch SEP20 token balance 

    try:
        # Get total SmartBch SEP20 token balance of the wallet
        api_response = api_instance.smart_bch_sep20_balance(smart_bch_sep20_balance_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_balance_request** | [**SmartBchSep20BalanceRequest**](SmartBchSep20BalanceRequest.md)| Request for a wallet SmartBch SEP20 token balance  | 

### Return type

[**SmartBchSep20BalanceResponse**](SmartBchSep20BalanceResponse.md)

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

# **smart_bch_sep20_deposit_address**
> SmartBchDepositAddressResponse smart_bch_sep20_deposit_address(serialized_wallet)

Get an SmartBch SEP20 deposit address

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for an SmartBch SEP20 deposit address given a wallet 

    try:
        # Get an SmartBch SEP20 deposit address
        api_response = api_instance.smart_bch_sep20_deposit_address(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for an SmartBch SEP20 deposit address given a wallet  | 

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

# **smart_bch_sep20_deposit_qr**
> ScalableVectorGraphic smart_bch_sep20_deposit_qr(serialized_wallet)

Get an SmartBch SEP20 receiving address as a qrcode

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    serialized_wallet = mainnet.SerializedWallet() # SerializedWallet | Request for a SmartBch SEP20 deposit address as a Quick Response code (qrcode) 

    try:
        # Get an SmartBch SEP20 receiving address as a qrcode
        api_response = api_instance.smart_bch_sep20_deposit_qr(serialized_wallet)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_deposit_qr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialized_wallet** | [**SerializedWallet**](SerializedWallet.md)| Request for a SmartBch SEP20 deposit address as a Quick Response code (qrcode)  | 

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

# **smart_bch_sep20_genesis**
> SmartBchSep20GenesisResponse smart_bch_sep20_genesis(smart_bch_sep20_genesis_request)

Get created tokenId back and new SmartBch SEP20 token balance of the wallet

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_genesis_request = mainnet.SmartBchSep20GenesisRequest() # SmartBchSep20GenesisRequest | Request to create a new SmartBch SEP20 token (genesis) 

    try:
        # Get created tokenId back and new SmartBch SEP20 token balance of the wallet
        api_response = api_instance.smart_bch_sep20_genesis(smart_bch_sep20_genesis_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_genesis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_genesis_request** | [**SmartBchSep20GenesisRequest**](SmartBchSep20GenesisRequest.md)| Request to create a new SmartBch SEP20 token (genesis)  | 

### Return type

[**SmartBchSep20GenesisResponse**](SmartBchSep20GenesisResponse.md)

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

# **smart_bch_sep20_mint**
> SmartBchSep20MintResponse smart_bch_sep20_mint(smart_bch_sep20_mint_request)

Get created tokenId back and new SmartBch SEP20 token balance of the wallet

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_mint_request = mainnet.SmartBchSep20MintRequest() # SmartBchSep20MintRequest | Request to mint more of SmartBch SEP20 tokens 

    try:
        # Get created tokenId back and new SmartBch SEP20 token balance of the wallet
        api_response = api_instance.smart_bch_sep20_mint(smart_bch_sep20_mint_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_mint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_mint_request** | [**SmartBchSep20MintRequest**](SmartBchSep20MintRequest.md)| Request to mint more of SmartBch SEP20 tokens  | 

### Return type

[**SmartBchSep20MintResponse**](SmartBchSep20MintResponse.md)

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

# **smart_bch_sep20_send**
> list[object] smart_bch_sep20_send(smart_bch_sep20_send_request)

Send some SmartBch SEP20 token amount to a given address

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_send_request = mainnet.SmartBchSep20SendRequest() # SmartBchSep20SendRequest | place a SmartBch SEP20 token send request

    try:
        # Send some SmartBch SEP20 token amount to a given address
        api_response = api_instance.smart_bch_sep20_send(smart_bch_sep20_send_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_send_request** | [**SmartBchSep20SendRequest**](SmartBchSep20SendRequest.md)| place a SmartBch SEP20 token send request | 

### Return type

**list[object]**

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

# **smart_bch_sep20_send_max**
> list[object] smart_bch_sep20_send_max(smart_bch_sep20_send_max_request)

Send all available SmartBch SEP20 token funds to a given address

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_send_max_request = mainnet.SmartBchSep20SendMaxRequest() # SmartBchSep20SendMaxRequest | Request to send all available SmartBch SEP20 token funds to a given address

    try:
        # Send all available SmartBch SEP20 token funds to a given address
        api_response = api_instance.smart_bch_sep20_send_max(smart_bch_sep20_send_max_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_send_max: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_send_max_request** | [**SmartBchSep20SendMaxRequest**](SmartBchSep20SendMaxRequest.md)| Request to send all available SmartBch SEP20 token funds to a given address | 

### Return type

**list[object]**

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

# **smart_bch_sep20_token_info**
> SmartBchSep20TokenInfoResponse smart_bch_sep20_token_info(smart_bch_sep20_token_info_request)

Get information about the SmartBch SEP20 token

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
    api_instance = mainnet.SmartbchSep20Api(api_client)
    smart_bch_sep20_token_info_request = mainnet.SmartBchSep20TokenInfoRequest() # SmartBchSep20TokenInfoRequest | Request to get information about the SmartBch SEP20 token 

    try:
        # Get information about the SmartBch SEP20 token
        api_response = api_instance.smart_bch_sep20_token_info(smart_bch_sep20_token_info_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmartbchSep20Api->smart_bch_sep20_token_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_bch_sep20_token_info_request** | [**SmartBchSep20TokenInfoRequest**](SmartBchSep20TokenInfoRequest.md)| Request to get information about the SmartBch SEP20 token  | 

### Return type

[**SmartBchSep20TokenInfoResponse**](SmartBchSep20TokenInfoResponse.md)

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

