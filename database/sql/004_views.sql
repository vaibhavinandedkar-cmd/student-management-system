CREATE VIEW student_details AS

SELECT

s.id,

s.student_code,

s.first_name,

s.last_name,

d.department_name,

s.semester,

s.email,

s.phone,

s.status

FROM students s

JOIN departments d

ON s.department_id=d.id;
