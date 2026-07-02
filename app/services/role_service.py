from app.repositories.role_repository import RoleRepository
from app.services.base_service import BaseService


class RoleService(BaseService):

    def __init__(self):
        super().__init__(RoleRepository())

    def get_by_name(self, role_name):
        return self.repository.get_by_name(role_name)
