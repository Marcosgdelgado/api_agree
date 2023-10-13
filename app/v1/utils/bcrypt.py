"""Bcrypt util"""

from passlib.context import CryptContext


class Bcrypt:
    """Bcrypt class"""

    def __init__(self):
        self.bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str):
        """Hash password"""
        return self.bcrypt_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        """Verify password"""
        return self.bcrypt_context.verify(plain_password, hashed_password)
