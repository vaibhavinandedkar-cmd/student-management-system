from app.config.database import db
from app.models.subject import Subject
from app.repositories.base_repository import BaseRepository


class SubjectRepository(BaseRepository):

    def __init__(self):
        super().__init__(Subject)

    def get_by_subject_code(self, subject_code):
        return self.first(subject_code=subject_code)

    def get_by_course(self, course_id):
        return self.filter_by(course_id=course_id)

    def get_by_faculty(self, faculty_id):
        return self.filter_by(faculty_id=faculty_id)

    def search(self, query):
        return Subject.query.filter(
            db.or_(
                Subject.subject_code.ilike(f"%{query}%"),
                Subject.subject_name.ilike(f"%{query}%")
            )
        ).order_by(Subject.id).all()
