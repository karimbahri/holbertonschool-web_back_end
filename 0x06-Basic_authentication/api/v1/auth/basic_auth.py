#!/usr/bin/env python3
"""basic_auth.py"""
from api.v1.auth.auth import Auth


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
