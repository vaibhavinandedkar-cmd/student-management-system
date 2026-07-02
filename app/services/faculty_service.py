from app.repositories.faculty_repository import FacultyRepository
from app.services.base_service import BaseService


class FacultyService(BaseService):

    def __init__(self):
        super().__init__(FacultyRepository())

    def get_by_faculty_code(self, faculty_code):
        return self.repository.get_by_faculty_code(faculty_code)

    def get_by_department(self, department_id):
        return self.repository.get_by_department(department_id)
