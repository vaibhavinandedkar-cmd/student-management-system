from typing import List, Optional

from app.config.database import db
from app.models.student import Student


class StudentRepository:
    """
    Repository responsible for all database operations
    related to the Student model.

    This class should ONLY contain database logic.
    No business logic should be implemented here.
    """

    def create(self, student: Student) -> Student:
        """
        Save a new student.
        """
        db.session.add(student)
        db.session.commit()
        return student

    def get_by_id(self, student_id: int) -> Optional[Student]:
        """
        Get student by primary key.
        """
        return Student.query.get(student_id)

    def get_by_student_code(
        self,
        student_code: str
    ) -> Optional[Student]:
        """
        Get student using student code.
        """
        return Student.query.filter_by(
            student_code=student_code
        ).first()

    def get_by_email(
        self,
        email: str
    ) -> Optional[Student]:
        """
        Get student using email.
        """
        return Student.query.filter_by(
            email=email
        ).first()

    def get_all(self) -> List[Student]:
        """
        Return all students.
        """
        return Student.query.order_by(
            Student.id
        ).all()

    def update(self) -> None:
        """
        Commit pending changes.
        """
        db.session.commit()

    def delete(self, student: Student) -> bool:
        """
        Delete student.
        """
        db.session.delete(student)
        db.session.commit()

    def exists(
        self,
        student_code: str
    ) -> bool:
        """
        Check whether a student exists.
        """
        return (
            Student.query.filter_by(
                student_code=student_code
            ).first()
            is not None
        )
