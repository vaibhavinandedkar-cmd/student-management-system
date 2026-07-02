from app.repositories.user_repository import UserRepository
from app.services.base_service import BaseService


class UserService(BaseService):

    def __init__(self):
        super().__init__(UserRepository())

    def get_by_username(self, username):
        return self.repository.get_by_username(username)

    def get_by_email(self, email):
        return self.repository.get_by_email(email)
