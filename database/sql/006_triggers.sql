CREATE TRIGGER trg_student_timestamp

BEFORE UPDATE

ON students

FOR EACH ROW

EXECUTE FUNCTION update_timestamp();
