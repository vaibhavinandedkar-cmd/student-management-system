from datetime import datetime

from app.config.database import db


class Student(db.Model):
    """
    Student Model
    Represents the students table.
    """

    __tablename__ = "students"

    # -------------------------
    # Primary Key
    # -------------------------

    student_id = db.Column(
        db.Integer,
        primary_key=True
    )

    # -------------------------
    # Basic Information
    # -------------------------

    first_name = db.Column(
        db.String(50),
        nullable=False
    )

    last_name = db.Column(
        db.String(50),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20)
    )

    date_of_birth = db.Column(
        db.Date
    )

    gender = db.Column(
        db.String(20)
    )

    admission_date = db.Column(
        db.Date,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Active"
    )

    # -------------------------
    # Audit Columns
    # -------------------------

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
