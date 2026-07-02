from app.config.database import db
from app.models.base_model import BaseModel


class Subject(BaseModel):
    __tablename__ = "subjects"

    subject_code = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    subject_name = db.Column(
        db.String(100),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    semester = db.Column(
        db.Integer,
        nullable=False
    )

    credits = db.Column(db.Integer)

    faculty_id = db.Column(
        db.Integer,
        db.ForeignKey("faculty.id")
    )

    course = db.relationship(
        "Course",
        back_populates="subjects"
    )
