from app.repositories.exam_repository import ExamRepository
from app.services.base_service import BaseService


class ExamService(BaseService):

    def __init__(self):
        super().__init__(ExamRepository())

    def search(self, query):
        return self.repository.search(query)

    def get_by_subject(self, subject_id):
        return self.repository.get_by_subject(subject_id)

    def get_by_exam_name(self, exam_name):
        return self.repository.get_by_exam_name(exam_name)
