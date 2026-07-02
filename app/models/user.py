from app.config.database import db
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    last_login = db.Column(db.DateTime)

    role = db.relationship(
        "Role",
        back_populates="users"
    )
