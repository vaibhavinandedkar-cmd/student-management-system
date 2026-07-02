from app.repositories.student_repository import StudentRepository
from app.services.base_service import BaseService


class StudentService(BaseService):

    def __init__(self):
        super().__init__(StudentRepository())

    def get_by_student_code(self, student_code):
        return self.repository.get_by_student_code(student_code)

    def get_by_email(self, email):
        return self.repository.get_by_email(email)

    def get_by_department(self, department_id):
        return self.repository.get_by_department(department_id)
