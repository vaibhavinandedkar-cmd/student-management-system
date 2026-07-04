from app.config.database import db
from app.models.course import Course
from app.repositories.base_repository import BaseRepository


class CourseRepository(BaseRepository):

    def __init__(self):
        super().__init__(Course)

    def get_by_course_code(self, course_code):
        return self.first(course_code=course_code)

    def get_by_department(self, department_id):
        return self.filter_by(department_id=department_id)

    def search(self, query):
        return Course.query.filter(
            db.or_(
                Course.course_code.ilike(f"%{query}%"),
                Course.course_name.ilike(f"%{query}%")
            )
        ).order_by(Course.id).all()
