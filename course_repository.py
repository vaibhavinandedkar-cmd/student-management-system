from app.models.course import Course
from app.repositories.base_repository import BaseRepository


class CourseRepository(BaseRepository):

    def __init__(self):
        super().__init__(Course)

    def get_by_course_code(self, course_code):
        return self.first(course_code=course_code)

    def get_by_department(self, department_id):
        return self.filter_by(department_id=department_id)
