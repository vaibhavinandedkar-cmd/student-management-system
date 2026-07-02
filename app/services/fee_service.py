from app.repositories.fee_repository import FeeRepository
from app.services.base_service import BaseService


class FeeService(BaseService):

    def __init__(self):
        super().__init__(FeeRepository())

    def get_by_student(self, student_id):
        return self.repository.get_by_student(student_id)
