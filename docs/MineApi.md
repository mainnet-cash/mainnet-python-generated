# mainnet.MineApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mine**](MineApi.md#mine) | **POST** /mine | Mine regtest coins to a specified address


# **mine**
> list[str] mine(mine_request=mine_request)

Mine regtest coins to a specified address

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
    api_instance = mainnet.MineApi(api_client)
    mine_request = mainnet.MineRequest() # MineRequest |  (optional)

    try:
        # Mine regtest coins to a specified address
        api_response = api_instance.mine(mine_request=mine_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MineApi->mine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mine_request** | [**MineRequest**](MineRequest.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | request accepted |  -  |
**400** | Invalid Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

