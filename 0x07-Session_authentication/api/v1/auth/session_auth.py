#!/usr/bin/env python3
"""session_auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth:
        class that inherit from Auth
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """create_session:
            instance method: create session
        """
        if user_id is None:
            return user_id
        if type(user_id) is not str:
            return None
        self.sessionId = str(uuid4())
        self.user_id_by_session_id[self.sessionId] = user_id
        return self.sessionId
