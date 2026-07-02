from app.repositories.audit_log_repository import AuditLogRepository
from app.services.base_service import BaseService


class AuditLogService(BaseService):

    def __init__(self):
        super().__init__(AuditLogRepository())

    def get_by_user(self, user_id):
        return self.repository.get_by_user(user_id)
