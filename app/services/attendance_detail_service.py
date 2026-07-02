from app.repositories.attendance_detail_repository import AttendanceDetailRepository
from app.services.base_service import BaseService


class AttendanceDetailService(BaseService):

    def __init__(self):
        super().__init__(AttendanceDetailRepository())

    def get_by_attendance(self, attendance_id):
        return self.repository.get_by_attendance(attendance_id)

    def get_by_student(self, student_id):
        return self.repository.get_by_student(student_id)
