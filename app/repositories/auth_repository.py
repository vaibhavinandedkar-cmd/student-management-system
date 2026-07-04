from app.config.database import db
from app.models.user import User


class AuthRepository:

    def get_by_username(
        self,
        username: str
    ):
        return User.query.filter_by(
            username=username
        ).first()

    def get_by_email(
        self,
        email: str
    ):
        return User.query.filter_by(
            email=email
        ).first()

    def save(self):
        db.session.commit()
