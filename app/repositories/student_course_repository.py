from app.models.student_course import StudentCourse
from app.repositories.base_repository import BaseRepository


class StudentCourseRepository(BaseRepository):

    def __init__(self):
        super().__init__(StudentCourse)

    def get_by_student(self, student_id):
        return self.filter_by(student_id=student_id)

    def get_by_course(self, course_id):
        return self.filter_by(course_id=course_id)
