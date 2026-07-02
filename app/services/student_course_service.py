from app.repositories.student_course_repository import StudentCourseRepository
from app.services.base_service import BaseService


class StudentCourseService(BaseService):

    def __init__(self):
        super().__init__(StudentCourseRepository())

    def get_by_student(self, student_id):
        return self.repository.get_by_student(student_id)

    def get_by_course(self, course_id):
        return self.repository.get_by_course(course_id)
