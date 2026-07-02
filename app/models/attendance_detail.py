from app.config.database import db
from app.models.base_model import BaseModel


class AttendanceDetail(BaseModel):
    __tablename__ = "attendance_details"

    attendance_id = db.Column(
        db.Integer,
        db.ForeignKey("attendance.id"),
        nullable=False
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False
    )

    remarks = db.Column(db.Text)

    attendance = db.relationship(
        "Attendance",
        back_populates="details"
    )

    student = db.relationship("Student")
