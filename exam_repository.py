from app.models.exam import Exam
from app.repositories.base_repository import BaseRepository


class ExamRepository(BaseRepository):

    def __init__(self):
        super().__init__(Exam)

    def get_by_subject(self, subject_id):
        return self.filter_by(subject_id=subject_id)

    def get_by_exam_name(self, exam_name):
        return self.filter_by(exam_name=exam_name)
