from app.models.user import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username):
        return self.first(username=username)

    def get_by_email(self, email):
        return self.first(email=email)
