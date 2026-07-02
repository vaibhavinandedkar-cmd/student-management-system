from app.config.database import db


class BaseRepository:
    """
    Generic repository.
    """

    def __init__(self, model):
        self.model = model

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, entity_id):
        return db.session.get(self.model, entity_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, entity):
        db.session.commit()
        return entity

    def delete(self, entity):
        db.session.delete(entity)
        db.session.commit()
        return True

    def exists(self, **filters):
        return self.model.query.filter_by(**filters).first() is not None

    def filter_by(self, **filters):
        return self.model.query.filter_by(**filters).all()

    def first(self, **filters):
        return self.model.query.filter_by(**filters).first()

    def count(self):
        return self.model.query.count()
