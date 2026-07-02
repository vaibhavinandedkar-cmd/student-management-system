from app.config.database import db
from app.models.base_model import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    role_name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(db.Text)

    users = db.relationship(
        "User",
        back_populates="role"
    )
