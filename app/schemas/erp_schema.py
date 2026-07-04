from marshmallow import Schema, fields, validate


class StudentFormSchema(Schema):
    student_code = fields.String(required=True, validate=validate.Length(min=3, max=20))
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    phone = fields.String(validate=validate.Length(max=15))
    gender = fields.String(validate=validate.Length(max=10))
    date_of_birth = fields.Date(format="%Y-%m-%d")
    department_id = fields.Integer(required=True)
    admission_date = fields.Date(format="%Y-%m-%d")
    semester = fields.Integer(validate=validate.Range(min=1, max=12))
    address = fields.String()
    status = fields.String(validate=validate.OneOf(["Active", "Inactive", "Pending"]))


class DepartmentFormSchema(Schema):
    department_code = fields.String(required=True, validate=validate.Length(min=2, max=20))
    department_name = fields.String(required=True, validate=validate.Length(min=2, max=100))
    hod_name = fields.String(validate=validate.Length(max=100))
    description = fields.String()
    status = fields.String(validate=validate.OneOf(["Active", "Inactive"]))


class FacultyFormSchema(Schema):
    faculty_code = fields.String(required=True, validate=validate.Length(min=3, max=20))
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    phone = fields.String(validate=validate.Length(max=15))
    gender = fields.String(validate=validate.Length(max=10))
    designation = fields.String(validate=validate.Length(max=100))
    department_id = fields.Integer(required=True)
    joining_date = fields.Date(format="%Y-%m-%d")
    salary = fields.Decimal(as_string=True)
    status = fields.String(validate=validate.OneOf(["Active", "Inactive", "On Leave"]))


class CourseFormSchema(Schema):
    course_code = fields.String(required=True, validate=validate.Length(min=2, max=20))
    course_name = fields.String(required=True, validate=validate.Length(min=2, max=100))
    department_id = fields.Integer(required=True)
    duration_years = fields.Integer(validate=validate.Range(min=1, max=10))
    total_semesters = fields.Integer(validate=validate.Range(min=1, max=20))
    status = fields.String(validate=validate.OneOf(["Active", "Inactive"]))


class SubjectFormSchema(Schema):
    subject_code = fields.String(required=True, validate=validate.Length(min=2, max=20))
    subject_name = fields.String(required=True, validate=validate.Length(min=2, max=100))
    course_id = fields.Integer(required=True)
    semester = fields.Integer(required=True, validate=validate.Range(min=1, max=12))
    credits = fields.Integer(validate=validate.Range(min=1, max=10))
    faculty_id = fields.Integer()
