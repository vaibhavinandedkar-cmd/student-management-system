from app.repositories.mark_repository import MarkRepository
from app.services.base_service import BaseService


class MarkService(BaseService):

    def __init__(self):
        super().__init__(MarkRepository())

    def get_by_student(self, student_id):
        return self.repository.get_by_student(student_id)

    def get_by_exam(self, exam_id):
        return self.repository.get_by_exam(exam_id)

    def get_student_exam(self, student_id, exam_id):
        return self.repository.get_student_exam(
            student_id,
            exam_id
        )
