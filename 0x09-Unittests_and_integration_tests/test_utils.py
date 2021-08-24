#!/usr/bin/env python3
"""test_utils"""
import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map
from utils import memoize


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize(self):
        """test_memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with mock.patch.object(TestClass, 'a_method') as mk:
            t_class = TestClass()
            self.assertEqual(t_class.a_property, mk.return_value)
            self.assertEqual(t_class.a_property, mk.return_value)
            mk.assert_called_once()


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


"""class TestGetJson(unittest.TestCase):
    TestGetJson class
        json requests tests
    """
