#!/usr/bin/env python3
"""encrypt_password.py"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password:
        a function that takes a password
        (string) and return a hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
