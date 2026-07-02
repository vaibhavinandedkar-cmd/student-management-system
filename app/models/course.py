from app.config.database import db
from app.models.base_model import BaseModel


class Course(BaseModel):
    __tablename__ = "courses"

    course_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    course_name = db.Column(
        db.String(100),
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    duration_years = db.Column(db.Integer)

    total_semesters = db.Column(db.Integer)

    status = db.Column(
        db.String(20),
        default="Active"
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )

    subjects = db.relationship(
        "Subject",
        back_populates="course"
    )

    students = db.relationship(
        "StudentCourse",
        back_populates="course"
    )
