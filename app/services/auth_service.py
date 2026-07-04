from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

from app.repositories.auth_repository import AuthRepository

bcrypt = Bcrypt()


class AuthService:

    def __init__(self):
        self.repository = AuthRepository()

    def hash_password(self, password: str):

        return bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

    def verify_password(
        self,
        password: str,
        password_hash: str
    ):

        return bcrypt.check_password_hash(
            password_hash,
            password
        )

    def login(
        self,
        username,
        password
    ):

        user = self.repository.get_by_username(
            username
        )

        if not user:
            return None

        if not self.verify_password(
            password,
            user.password_hash
        ):
            return None

        user.last_login = datetime.utcnow()

        self.repository.update()

        token = create_access_token(
            identity=user.id
        )

        return {
            "user": user,
            "token": token
        }
