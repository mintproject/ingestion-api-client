# ingestion-api [![Build Status](https://travis-ci.org/mintproject/model-catalog-python-api-client.svg?branch=master)](https://travis-ci.org/mintproject/model-catalog-python-api-client)
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.2.0
- Package version: 1.3.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install ingestion-api
```
(you may need to run `pip` with root permission: `sudo pip install ingestion-api`)

Then import the package:
```python
import ingestion 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ingestion
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import ingestion
from ingestion.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = ingestion.DefaultApi(ingestion.ApiClient(configuration))
modelthread = ingestion.Modelthread() # Modelthread | A new `modelthread` to be created.

try:
    # Create a modelthread
    api_instance.modelthreads_post(modelthread)
except ApiException as e:
    print("Exception when calling DefaultApi->modelthreads_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ingestion.mint.isi.edu/v1.2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**modelthreads_post**](docs/DefaultApi.md#modelthreads_post) | **POST** /modelthreads | Create a modelthread
*ResultApi* | [**results_thread_id_get**](docs/ResultApi.md#results_thread_id_get) | **GET** /results/{thread_id} | Get a result
*SummaryApi* | [**summary_get**](docs/SummaryApi.md#summary_get) | **GET** /summary | List All summary
*SummaryApi* | [**summary_post**](docs/SummaryApi.md#summary_post) | **POST** /summary | Create a summary
*SummaryApi* | [**summary_thread_id_get**](docs/SummaryApi.md#summary_thread_id_get) | **GET** /summary/{thread_id} | Get a Summary


## Documentation For Models

 - [Modelthread](docs/Modelthread.md)
 - [ProblemFormulation](docs/ProblemFormulation.md)
 - [Scenario](docs/Scenario.md)
 - [Summary](docs/Summary.md)
 - [SummaryResponse](docs/SummaryResponse.md)
 - [Thread](docs/Thread.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




