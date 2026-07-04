from app.models.student import Student
from app.repositories.base_repository import BaseRepository


class StudentRepository(BaseRepository):

    def __init__(self):
        super().__init__(Student)

    def get_by_student_code(self, student_code):
        return self.first(student_code=student_code)

    def get_by_email(self, email):
        return self.first(email=email)

    def get_by_department(self, department_id):
        return self.filter_by(department_id=department_id)
