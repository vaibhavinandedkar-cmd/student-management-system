from app.config.database import db
from app.models.base_model import BaseModel


class Student(BaseModel):
    __tablename__ = "students"

    student_code = db.Column(db.String(20), unique=True, nullable=False)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(15))

    gender = db.Column(db.String(10))

    date_of_birth = db.Column(db.Date)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    admission_date = db.Column(db.Date)

    semester = db.Column(db.Integer)

    address = db.Column(db.Text)

    status = db.Column(
        db.String(20),
        default="Active"
    )

    department = db.relationship(
        "Department",
        back_populates="students"
    )

    courses = db.relationship(
        "StudentCourse",
        back_populates="student",
        cascade="all, delete-orphan"
    )
