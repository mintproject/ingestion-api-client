# ingestion.DefaultApi

All URIs are relative to *https://ingestion.mint.isi.edu/v1.2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelthreads_post**](DefaultApi.md#modelthreads_post) | **POST** /modelthreads | Create a modelthread


# **modelthreads_post**
> modelthreads_post(modelthread)

Create a modelthread

Creates a new instance of a `modelthread`.

### Example

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ingestion.DefaultApi()
modelthread = ingestion.Modelthread() # Modelthread | A new `modelthread` to be created.

try:
    # Create a modelthread
    api_instance.modelthreads_post(modelthread)
except ApiException as e:
    print("Exception when calling DefaultApi->modelthreads_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modelthread** | [**Modelthread**](Modelthread.md)| A new &#x60;modelthread&#x60; to be created. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

