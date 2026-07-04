from app.repositories.department_repository import DepartmentRepository
from app.services.base_service import BaseService


class DepartmentService(BaseService):

    def __init__(self):
        super().__init__(DepartmentRepository())

    def search(self, query):
        return self.repository.search(query)

    def get_by_code(self, code):
        return self.repository.get_by_code(code)
