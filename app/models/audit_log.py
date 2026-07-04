from app.config.database import db
from app.models.base_model import BaseModel


class AuditLog(BaseModel):
    __tablename__ = "audit_logs"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    action = db.Column(
        db.String(100),
        nullable=False
    )

    entity_name = db.Column(
        db.String(100),
        nullable=False
    )

    entity_id = db.Column(db.Integer)

    ip_address = db.Column(db.String(50))

    user = db.relationship("User")
