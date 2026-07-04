from app.models.user import User


class AuthRepository:

    def get_by_username(
        self,
        username
    ):
        return User.query.filter_by(
            username=username
        ).first()

    def get_by_email(
        self,
        email
    ):
        return User.query.filter_by(
            email=email
        ).first()

    def update(self):
        from app.config.database import db
        db.session.commit()
