from app.config.database import db
from app.models.base_model import BaseModel


class Exam(BaseModel):
    __tablename__ = "exams"

    exam_name = db.Column(
        db.String(100),
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    exam_type = db.Column(db.String(50))

    exam_date = db.Column(db.Date)

    total_marks = db.Column(db.Integer)

    marks = db.relationship(
        "Mark",
        back_populates="exam",
        cascade="all, delete-orphan"
    )
