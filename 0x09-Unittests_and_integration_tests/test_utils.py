#!/usr/bin/env python3
"""test_utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap
    unit test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, t_map, t_path, t_expected):
        """test method : test access_nested_map"""
        self.assertEqual(access_nested_map(t_map, t_path), t_expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, t_map, t_path):
        """
        test_access_nested_map_exception
        raise exception
        test method:"""
        self.assertRaises(KeyError, access_nested_map, t_map, t_path)
