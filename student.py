students = {}


def add_student(student_id, name):
    return False


def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False


def search_student(student_id):
    if student_id in students:
        return f"Student Found: {students[student_id]}"
    return "Student Not Found in Database"


def update_student(student_id, new_name):
    if student_id in students:
        students[student_id] = new_name
        return True
    return False
