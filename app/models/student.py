from datetime import datetime

from app.config.database import db


class Student(db.Model):
    """
    Student Model
    """

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_code = db.Column(
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

    phone = db.Column(
        db.String(15)
    )

    gender = db.Column(
        db.String(10)
    )

    department = db.Column(
        db.String(100)
    )

    semester = db.Column(
        db.Integer
    )

    address = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Student {self.student_code}>"
