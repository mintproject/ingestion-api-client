# ingestion.ResultApi

All URIs are relative to *https://ingestion.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**results_thread_id_get**](ResultApi.md#results_thread_id_get) | **GET** /results/{thread_id} | Get a result


# **results_thread_id_get**
> object results_thread_id_get(thread_id)

Get a result

Gets the details of a single instance of a results

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.ResultApi()
thread_id = 'thread_id_example' # str | The ID of the resource

try:
    # Get a result
    api_response = api_instance.results_thread_id_get(thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->results_thread_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the resource | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

