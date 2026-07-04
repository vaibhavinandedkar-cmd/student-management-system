from app.config.database import db
from app.models.base_model import BaseModel


class Payment(BaseModel):
    __tablename__ = "payments"

    fee_id = db.Column(
        db.Integer,
        db.ForeignKey("fees.id"),
        nullable=False
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    payment_mode = db.Column(db.String(50))

    transaction_reference = db.Column(db.String(100))

    payment_date = db.Column(db.DateTime)

    fee = db.relationship(
        "Fee",
        back_populates="payments"
    )
