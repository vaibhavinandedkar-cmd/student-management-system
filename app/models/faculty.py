from app.config.database import db
from app.models.base_model import BaseModel


class Faculty(BaseModel):
    __tablename__ = "faculty"

    faculty_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(db.String(15))

    gender = db.Column(db.String(10))

    designation = db.Column(db.String(100))

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    joining_date = db.Column(db.Date)

    salary = db.Column(db.Numeric(10, 2))

    status = db.Column(
        db.String(20),
        default="Active"
    )

    department = db.relationship(
        "Department",
        back_populates="faculty"
    )
