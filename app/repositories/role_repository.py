from app.models.role import Role
from app.repositories.base_repository import BaseRepository


class RoleRepository(BaseRepository):

    def __init__(self):
        super().__init__(Role)

    def get_by_name(self, role_name):
        return self.first(role_name=role_name)
