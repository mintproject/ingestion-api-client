# ingestion.ThreadApi

All URIs are relative to *http://localhost:8080/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getthreads**](ThreadApi.md#getthreads) | **GET** /modelthreads | List All threads
[**modelthreads_thread_id_get**](ThreadApi.md#modelthreads_thread_id_get) | **GET** /modelthreads/{thread_id} | Get a Thread


# **getthreads**
> list[Thread] getthreads(limit, page=page, model=model)

List All threads

Gets a list of all `thread` entities.

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.ThreadApi()
limit = 200 # int |  (default to 200)
page = 1 # int |  (optional) (default to 1)
model = 'model_example' # str |  (optional)

try:
    # List All threads
    api_response = api_instance.getthreads(limit, page=page, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreadApi->getthreads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [default to 200]
 **page** | **int**|  | [optional] [default to 1]
 **model** | **str**|  | [optional] 

### Return type

[**list[Thread]**](Thread.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modelthreads_thread_id_get**
> Thread modelthreads_thread_id_get(thread_id)

Get a Thread

Gets the details of a single instance of a Thread

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.ThreadApi()
thread_id = 'thread_id_example' # str | The ID of the resource

try:
    # Get a Thread
    api_response = api_instance.modelthreads_thread_id_get(thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreadApi->modelthreads_thread_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the resource | 

### Return type

[**Thread**](Thread.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

