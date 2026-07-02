from app.config.database import db
from app.models.base_model import BaseModel


class StudentCourse(BaseModel):
    __tablename__ = "student_courses"

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    academic_year = db.Column(db.String(20))

    semester = db.Column(db.Integer)

    student = db.relationship(
        "Student",
        back_populates="courses"
    )

    course = db.relationship(
        "Course",
        back_populates="students"
    )
