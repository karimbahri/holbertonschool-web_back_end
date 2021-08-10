#!/usr/bin/env python3
"""basic_auth.py"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """BasicAuth:
        class that inherit from auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract authorization
            public method: return 64base authorization
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic'):
            return None
        authorization64_header = authorization_header[6:]
        return authorization64_header

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """decode_base64_authorization_header:
            public method
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return b64decode(base64_authorization_header)\
                            .decode('utf-8')
        except Exception:
            return None
