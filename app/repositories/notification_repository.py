from app.models.notification import Notification
from app.repositories.base_repository import BaseRepository


class NotificationRepository(BaseRepository):

    def __init__(self):
        super().__init__(Notification)

    def get_by_user(self, user_id):
        return self.filter_by(user_id=user_id)
