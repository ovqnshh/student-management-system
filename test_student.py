import pytest
from student import *


def setup_function():
    students.clear()


def test_add_student():
    assert add_student(1, "Vansh") == True


def test_add_duplicate_student():
    add_student(1, "Vansh")
    assert add_student(1, "Vansh") == False


def test_search_existing_student():
    add_student(1, "Vansh")
    assert search_student(1) == "Student Found: Vansh"


def test_search_non_existing_student():
    assert search_student(99) == "Student Not Found"


def test_remove_existing_student():
    add_student(1, "Vansh")
    assert remove_student(1) == True


def test_remove_non_existing_student():
    assert remove_student(99) == False


def test_update_existing_student():
    add_student(1, "Vansh")
    assert update_student(1, "Aman") == True


def test_update_non_existing_student():
    assert update_student(99, "Aman") == False


def test_student_data_after_update():
    add_student(1, "Vansh")
    update_student(1, "Aman")
    assert students[1] == "Aman"


def test_multiple_students():
    add_student(1, "Vansh")
    add_student(2, "Aman")
    assert len(students) == 2
