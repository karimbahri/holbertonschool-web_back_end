#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request
"""Auth class"""


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
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header:
            return authorization header request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user:
        return: TypeVar
        """
        return None
