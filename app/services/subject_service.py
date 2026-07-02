from app.repositories.subject_repository import SubjectRepository
from app.services.base_service import BaseService


class SubjectService(BaseService):

    def __init__(self):
        super().__init__(SubjectRepository())

    def get_by_subject_code(self, subject_code):
        return self.repository.get_by_subject_code(subject_code)

    def get_by_course(self, course_id):
        return self.repository.get_by_course(course_id)

    def get_by_faculty(self, faculty_id):
        return self.repository.get_by_faculty(faculty_id)
