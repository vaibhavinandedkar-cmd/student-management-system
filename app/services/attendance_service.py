from app.repositories.attendance_repository import AttendanceRepository
from app.services.base_service import BaseService


class AttendanceService(BaseService):

    def __init__(self):
        super().__init__(AttendanceRepository())

    def get_by_subject(self, subject_id):
        return self.repository.get_by_subject(subject_id)

    def get_by_faculty(self, faculty_id):
        return self.repository.get_by_faculty(faculty_id)

    def get_by_date(self, attendance_date):
        return self.repository.get_by_date(attendance_date)
