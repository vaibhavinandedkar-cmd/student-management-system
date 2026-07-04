from app.config.database import db
from app.models.department import Department
from app.repositories.base_repository import BaseRepository


class DepartmentRepository(BaseRepository):

    def __init__(self):
        super().__init__(Department)

    def get_by_code(self, department_code):
        return self.first(department_code=department_code)

    def get_by_name(self, department_name):
        return self.first(department_name=department_name)

    def search(self, query):
        return Department.query.filter(
            db.or_(
                Department.department_code.ilike(f"%{query}%"),
                Department.department_name.ilike(f"%{query}%"),
                Department.hod_name.ilike(f"%{query}%")
            )
        ).order_by(Department.id).all()
