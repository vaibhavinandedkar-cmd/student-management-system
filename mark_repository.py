from app.models.mark import Mark
from app.repositories.base_repository import BaseRepository


class MarkRepository(BaseRepository):

    def __init__(self):
        super().__init__(Mark)

    def get_by_student(self, student_id):
        return self.filter_by(student_id=student_id)

    def get_by_exam(self, exam_id):
        return self.filter_by(exam_id=exam_id)

    def get_student_exam(self, student_id, exam_id):
        return self.first(
            student_id=student_id,
            exam_id=exam_id
        )
