from app.models.audit_log import AuditLog
from app.repositories.base_repository import BaseRepository


class AuditLogRepository(BaseRepository):

    def __init__(self):
        super().__init__(AuditLog)

    def get_by_user(self, user_id):
        return self.filter_by(user_id=user_id)
