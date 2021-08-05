#!/usr/bin/env python3
"""Auth class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
        API authentication

        public methods:
            require_auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth:
            check for authentication
            return boolean
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header:
            return authorization header request
        """
        if not request:
            return request
        authorization = request.headers.get('Authorization')
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user:
        return: TypeVar
        """
        return None
