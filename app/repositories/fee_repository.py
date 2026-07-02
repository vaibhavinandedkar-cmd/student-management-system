from app.models.fee import Fee
from app.repositories.base_repository import BaseRepository


class FeeRepository(BaseRepository):

    def __init__(self):
        super().__init__(Fee)

    def get_by_student(self, student_id):
        return self.filter_by(student_id=student_id)
