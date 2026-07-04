from app.config.database import db
from app.models.base_model import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    user = db.relationship("User")
