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

    is_verified = db.Column(
    db.Boolean,
    default=False
    )

    failed_login_attempts = db.Column(
    db.Integer,
    default=0
    ) 

    locked_until = db.Column(
    db.DateTime,
    nullable=True
    )

    password_changed_at = db.Column(
    db.DateTime
    )
