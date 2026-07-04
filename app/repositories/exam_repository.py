from app.config.database import db
from app.models.exam import Exam
from app.repositories.base_repository import BaseRepository


class ExamRepository(BaseRepository):

    def __init__(self):
        super().__init__(Exam)

    def get_by_subject(self, subject_id):
        return self.filter_by(subject_id=subject_id)

    def get_by_exam_name(self, exam_name):
        return self.first(exam_name=exam_name)

    def search(self, query):
        return Exam.query.filter(
            db.or_(
                Exam.exam_name.ilike(f"%{query}%"),
                db.cast(Exam.exam_date, db.String).ilike(f"%{query}%")
            )
        ).order_by(Exam.id).all()
