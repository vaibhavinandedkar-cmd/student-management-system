from app.repositories.payment_repository import PaymentRepository
from app.services.base_service import BaseService


class PaymentService(BaseService):

    def __init__(self):
        super().__init__(PaymentRepository())

    def get_by_fee(self, fee_id):
        return self.repository.get_by_fee(fee_id)
