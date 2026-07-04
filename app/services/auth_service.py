from datetime import datetime

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token

from app.repositories.auth_repository import AuthRepository


class AuthService:

    def __init__(self):
        self.repository = AuthRepository()

    def hash_password(self, password: str) -> str:
        """
        Encrypt password before saving.
        """
        return generate_password_hash(password).decode("utf-8")

    def verify_password(
        self,
        password: str,
        password_hash: str
    ) -> bool:
        """
        Verify user password.
        """
        return check_password_hash(
            password_hash,
            password
        )

    def login(
        self,
        username: str,
        password: str
    ):

        user = self.repository.get_by_username(
            username
        )

        if not user:
            return None

        if not user.is_active:
            return None

        if not self.verify_password(
            password,
            user.password_hash
        ):
            return None

        user.last_login = datetime.utcnow()

        self.repository.save()

        token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "username": user.username,
                "role": user.role.role_name
            }
        )

        return {
            "access_token": token,
            "user": user
        }
