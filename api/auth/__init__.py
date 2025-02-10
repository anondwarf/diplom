"""
This module initializes the authentication package by importing and exposing
the Register, Login, and User classes.
Classes:
    Register: Handles user registration.
    Login: Handles user login.
    User: Represents a user in the system.
__all__:
    A list of public objects of this module, as interpreted by `import *`.
"""

from .register import Register
from .login import Login
from .user import User

__all__ = ["Register", "Login", "User"]
