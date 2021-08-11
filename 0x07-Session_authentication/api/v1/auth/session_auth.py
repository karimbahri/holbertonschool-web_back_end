#!/usr/bin/env python3
"""session_auth"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id:
            return user based on session id
        """
        if session_id is None:
            return session_id
        if type(session_id) is not str:
            return None
        else:
            return self.user_id_by_session_id[session_id]

    def current_user(self, request=None):
        """current_user:
        return: TypeVar
        """
        cookie = self.session_cookie(request)
        usr_id = self.user_id_for_session_id(cookie)
        return User[usr_id]
