# coding: utf-8

"""
    ingestion

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ingestion
from ingestion.api.result_api import ResultApi  # noqa: E501
from ingestion.rest import ApiException


class TestResultApi(unittest.TestCase):
    """ResultApi unit test stubs"""

    def setUp(self):
        self.api = ingestion.api.result_api.ResultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_results_thread_id_get(self):
        """Test case for results_thread_id_get

        Get a result  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
