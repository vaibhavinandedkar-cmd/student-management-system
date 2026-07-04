from app.models.department import Department
from app.repositories.base_repository import BaseRepository


class DepartmentRepository(BaseRepository):

    def __init__(self):
        super().__init__(Department)

    def get_by_code(self, code):
        return self.first(department_code=code)
