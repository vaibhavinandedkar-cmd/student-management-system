from app.config.database import db
from app.models.base_model import BaseModel


class Fee(BaseModel):
    __tablename__ = "fees"

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    academic_year = db.Column(db.String(20))

    total_amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    due_amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    student = db.relationship("Student")

    payments = db.relationship(
        "Payment",
        back_populates="fee",
        cascade="all, delete-orphan"
    )
