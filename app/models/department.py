from app.config.database import db
from app.models.base_model import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    department_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    department_name = db.Column(
        db.String(100),
        nullable=False
    )

    hod_name = db.Column(db.String(100))

    description = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="Active"
    )

    faculty = db.relationship(
        "Faculty",
        back_populates="department"
    )

    students = db.relationship(
        "Student",
        back_populates="department"
    )

    courses = db.relationship(
        "Course",
        back_populates="department"
    )
