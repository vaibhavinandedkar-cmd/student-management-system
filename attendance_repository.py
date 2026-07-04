from app.models.attendance import Attendance
from app.repositories.base_repository import BaseRepository


class AttendanceRepository(BaseRepository):

    def __init__(self):
        super().__init__(Attendance)

    def get_by_subject(self, subject_id):
        return self.filter_by(subject_id=subject_id)

    def get_by_faculty(self, faculty_id):
        return self.filter_by(faculty_id=faculty_id)

    def get_by_date(self, attendance_date):
        return self.filter_by(attendance_date=attendance_date)
