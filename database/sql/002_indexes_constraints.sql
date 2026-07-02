CREATE INDEX idx_students_department
ON students(department_id);

CREATE INDEX idx_students_email
ON students(email);

CREATE INDEX idx_students_code
ON students(student_code);

CREATE INDEX idx_faculty_department
ON faculty(department_id);

CREATE INDEX idx_faculty_email
ON faculty(email);

CREATE INDEX idx_courses_department
ON courses(department_id);

CREATE INDEX idx_courses_code
ON courses(course_code);

CREATE INDEX idx_subject_course
ON subjects(course_id);

CREATE INDEX idx_subject_faculty
ON subjects(faculty_id);

CREATE INDEX idx_attendance_subject
ON attendance(subject_id);

CREATE INDEX idx_attendance_faculty
ON attendance(faculty_id);

CREATE INDEX idx_attendance_date
ON attendance(attendance_date);

CREATE INDEX idx_marks_student
ON marks(student_id);

CREATE INDEX idx_marks_exam
ON marks(exam_id);

CREATE INDEX idx_payment_fee
ON payments(fee_id);

CREATE INDEX idx_notification_user
ON notifications(user_id);

CREATE INDEX idx_audit_user
ON audit_logs(user_id);


