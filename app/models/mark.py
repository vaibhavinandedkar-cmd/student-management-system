from app.config.database import db
from app.models.base_model import BaseModel


class Mark(BaseModel):
    __tablename__ = "marks"

    exam_id = db.Column(
        db.Integer,
        db.ForeignKey("exams.id"),
        nullable=False
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    marks_obtained = db.Column(
        db.Numeric(5, 2)
    )

    grade = db.Column(db.String(5))

    remarks = db.Column(db.Text)

    exam = db.relationship(
        "Exam",
        back_populates="marks"
    )

    student = db.relationship("Student")
