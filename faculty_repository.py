from app.models.faculty import Faculty
from app.repositories.base_repository import BaseRepository


class FacultyRepository(BaseRepository):

    def __init__(self):
        super().__init__(Faculty)

    def get_by_faculty_code(self, faculty_code):
        return self.first(faculty_code=faculty_code)

    def get_by_department(self, department_id):
        return self.filter_by(department_id=department_id)
