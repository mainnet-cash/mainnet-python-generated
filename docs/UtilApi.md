# mainnet.UtilApi

All URIs are relative to *https://rest-unstable.mainnet.cash*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert**](UtilApi.md#convert) | **POST** /util/convert | convert between units


# **convert**
> float convert(convert_request=convert_request)

convert between units

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
    api_instance = mainnet.UtilApi(api_client)
    convert_request = mainnet.ConvertRequest() # ConvertRequest |  (optional)

    try:
        # convert between units
        api_response = api_instance.convert(convert_request=convert_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UtilApi->convert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_request** | [**ConvertRequest**](ConvertRequest.md)|  | [optional] 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

