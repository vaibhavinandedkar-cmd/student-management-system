from app.config.database import db
from app.models.base_model import BaseModel


class Attendance(BaseModel):
    __tablename__ = "attendance"

    attendance_date = db.Column(
        db.Date,
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    faculty_id = db.Column(
        db.Integer,
        db.ForeignKey("faculty.id"),
        nullable=False
    )

    semester = db.Column(
        db.Integer,
        nullable=False
    )

    details = db.relationship(
        "AttendanceDetail",
        back_populates="attendance",
        cascade="all, delete-orphan"
    )
