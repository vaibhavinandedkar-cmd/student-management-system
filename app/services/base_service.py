class BaseService:
    """
    Generic service layer.
    """

    def __init__(self, repository):
        self.repository = repository

    def create(self, entity):
        return self.repository.create(entity)

    def get_by_id(self, entity_id):
        return self.repository.get_by_id(entity_id)

    def get_all(self):
        return self.repository.get_all()

    def update(self, entity):
        return self.repository.update(entity)

    def delete(self, entity):
        return self.repository.delete(entity)

    def exists(self, **filters):
        return self.repository.exists(**filters)

    def filter_by(self, **filters):
        return self.repository.filter_by(**filters)

    def first(self, **filters):
        return self.repository.first(**filters)

    def count(self):
        return self.repository.count()
