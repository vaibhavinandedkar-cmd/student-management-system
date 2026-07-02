from app.models.attendance_detail import AttendanceDetail
from app.repositories.base_repository import BaseRepository


class AttendanceDetailRepository(BaseRepository):

    def __init__(self):
        super().__init__(AttendanceDetail)

    def get_by_attendance(self, attendance_id):
        return self.filter_by(attendance_id=attendance_id)

    def get_by_student(self, student_id):
        return self.filter_by(student_id=student_id)
