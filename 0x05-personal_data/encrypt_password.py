#!/usr/bin/env python3
"""encrypt_password.py"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password:
        a function that takes a password
        (string) and return a hashed password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid
        check the matching password with the hashed version
        it expects hashed_password(bytes) and password str
        as arguments
        and return a boolean (true/false)
    """
    return bcrypt.checkpw(password, hashed_password)
