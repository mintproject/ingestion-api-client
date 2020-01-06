# ingestion.SummaryApi

All URIs are relative to *http://localhost:8080/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summary_get**](SummaryApi.md#summary_get) | **GET** /summary | List All summary
[**summary_thread_id_get**](SummaryApi.md#summary_thread_id_get) | **GET** /summary/{thread_id} | Get a Summary


# **summary_get**
> list[Summary] summary_get(limit, page=page, model=model)

List All summary

Gets a list of all `summary` entities.

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.SummaryApi()
limit = 200 # int |  (default to 200)
page = 1 # int |  (optional) (default to 1)
model = '' # str |  (optional) (default to '')

try:
    # List All summary
    api_response = api_instance.summary_get(limit, page=page, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [default to 200]
 **page** | **int**|  | [optional] [default to 1]
 **model** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**list[Summary]**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summary_thread_id_get**
> Summary summary_thread_id_get(thread_id)

Get a Summary

Gets the details of a single instance of a summary

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.SummaryApi()
thread_id = 'thread_id_example' # str | The ID of the resource

try:
    # Get a Summary
    api_response = api_instance.summary_thread_id_get(thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryApi->summary_thread_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| The ID of the resource | 

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
