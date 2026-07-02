from typing import List, Optional

from app.models.student import Student
from app.repositories.student_repository import StudentRepository


class StudentService:
    """
    Service layer responsible for student business logic.
    """

    def __init__(self):
        self.student_repository = StudentRepository()

    def create_student(
        self,
        student: Student
    ) -> Student:
        """
        Create a new student.

        Business Rules:
        - Student code must be unique.
        - Email must be unique.
        """

        if self.student_repository.get_by_student_code(
            student.student_code
        ):
            raise ValueError(
                "Student code already exists."
            )

        if self.student_repository.get_by_email(
            student.email
        ):
            raise ValueError(
                "Email already exists."
            )

        return self.student_repository.create(student)

    def get_student_by_id(
        self,
        student_id: int
    ) -> Optional[Student]:
        """
        Retrieve a student by ID.
        """
        return self.student_repository.get_by_id(student_id)

    def get_all_students(
        self
    ) -> List[Student]:
        """
        Retrieve all students.
        """
        return self.student_repository.get_all()

    def update_student(
        self
    ) -> None:
        """
        Commit student changes.
        """
        self.student_repository.update()

    def delete_student(
        self,
        student: Student
    ) -> None:
        """
        Delete a student.
        """
        self.student_repository.delete(student)
