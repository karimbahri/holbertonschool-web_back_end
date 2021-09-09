#!/usr/bin/env python3
"""test"""
from utils import access_nested_map
from utils import get_json

if __name__ == "__main__":
    print(access_nested_map({"a": 1}, ("a",)))
    print(access_nested_map({"a": {"b": 2}}, ("a",)))
    print(access_nested_map({"a": {"b": 2}}, ("a", "b")))
