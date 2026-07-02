from app.models.payment import Payment
from app.repositories.base_repository import BaseRepository


class PaymentRepository(BaseRepository):

    def __init__(self):
        super().__init__(Payment)

    def get_by_fee(self, fee_id):
        return self.filter_by(fee_id=fee_id)
