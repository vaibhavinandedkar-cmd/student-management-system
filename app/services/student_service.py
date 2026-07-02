from typing import List, Optional

from app.models.student import Student
from app.repositories.student_repository import StudentRepository


class StudentService:
    """
    Service layer responsible for student business logic.
    """

    def __init__(self):
        self.student_repository = StudentRepository()

    def create_student(self, student: Student) -> Student:
        """
        Create a new student.
        """

        if self.student_repository.get_by_student_code(student.student_code):
            raise ValueError("Student code already exists.")

        if self.student_repository.get_by_email(student.email):
            raise ValueError("Email already exists.")

        return self.student_repository.create(student)

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """
        Retrieve student by ID.
        """
        return self.student_repository.get_by_id(student_id)

    def get_all_students(self) -> List[Student]:
        """
        Retrieve all students.
        """
        return self.student_repository.get_all()

    def update_student(self, student_id: int, data: dict) -> Optional[Student]:
        """
        Update student.
        """

        student = self.student_repository.get_by_id(student_id)

        if not student:
            return None

        for key, value in data.items():
            setattr(student, key, value)

        return self.student_repository.update(student)

    def delete_student(self, student_id: int) -> bool:
        """
        Delete student.
        """

        student = self.student_repository.get_by_id(student_id)

        if not student:
            return False

        return self.student_repository.delete(student)
