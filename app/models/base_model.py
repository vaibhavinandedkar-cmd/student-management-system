from datetime import datetime

from app.config.database import db


class BaseModel(db.Model):
    """
    Base model for all database tables.
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
