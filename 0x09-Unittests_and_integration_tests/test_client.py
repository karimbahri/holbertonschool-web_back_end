#!/usr/bin/env python3
"""test client"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient:
        class for client testing
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, t_name, t_mock):
        """test_org:
        public method to test
        GithubOrgClient.org
        """
        res = GithubOrgClient(t_name).org
        self.assertEqual(res, t_mock.return_value)
        t_mock.assert_called_once
