from django.test import TestCase
from CS361_Project.models import Supervisor


class test_Supervisor(TestCase):

    def setUp(self):
        self.supervisor = Supervisor()

    # Tests for createCourse
    def test_CreateTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.supervisor.createCourse("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_CreateTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.supervisor.createCourse("CompSci", 150)

    def test_CreateWrongDepartmentType(self):
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.supervisor.createCourse(25, 150)

    def test_CreateWrongCourseNumType(self):
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.supervisor.createCourse("CompSci", "150")

    def test_CreateNoParameters(self):
        with self.assertRaises(TypeError, msg="There are no parameters"):
            self.supervisor.createCourse()

    # Tests for deleteCourse
    def test_DeleteTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.supervisor.deleteCourse("CompSci", 150, "Survey of Computer Science")

    def test_DeleteTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.supervisor.deleteCourse("CompSci")

    def test_DeleteWrongDepartmentType(self):
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.supervisor.deleteCourse(25, 150)

    def test_DeleteWrongCourseNumType(self):
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.supervisor.deleteCourse("CompSci", "150")

    def test_DeleteNoParameters(self):
        with self.assertRaises(TypeError, msg="There are no parameters"):
            self.supervisor.deleteCourse()

    # Tests for editCourse
    def test_EditTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.supervisor.editCourse("CompSci", 150, "Survey of Computer Science")

    def test_EditTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.supervisor.editCourse("CompSci")

    def test_EditWrongDepartmentType(self):
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.supervisor.editCourse(25, 150)

    def test_EditWrongCourseNumType(self):
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.supervisor.editCourse("CompSci", "150")

    def test_EditNoParameters(self):
        with self.assertRaises(TypeError, msg="There are no parameters"):
            self.supervisor.editCourse()
