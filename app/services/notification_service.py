from app.repositories.notification_repository import NotificationRepository
from app.services.base_service import BaseService


class NotificationService(BaseService):

    def __init__(self):
        super().__init__(NotificationRepository())

    def get_by_user(self, user_id):
        return self.repository.get_by_user(user_id)
