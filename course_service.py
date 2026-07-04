from app.repositories.course_repository import CourseRepository
from app.services.base_service import BaseService


class CourseService(BaseService):

    def __init__(self):
        super().__init__(CourseRepository())

    def get_by_course_code(self, course_code):
        return self.repository.get_by_course_code(course_code)

    def get_by_department(self, department_id):
        return self.repository.get_by_department(department_id)
