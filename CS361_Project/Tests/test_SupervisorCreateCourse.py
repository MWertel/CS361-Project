from django.test import TestCase
from CS361_Project.models import Supervisor


class test_SupervisorCreateCourse(TestCase):

    def setUp(self):
        self.supervisor = Supervisor()

    def test_CorrectArgs(self):
        pass

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.supervisor.createCourse("CompSci", 150, "Survey of Computer Science", "Soronson", 1300)

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.supervisor.createCourse("CompSci", 150)

    def test_WrongDepartmentType(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.supervisor.createCourse(25, 150)

    def test_WrongCourseNumType(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.supervisor.createCourse("CompSci", "150")

    def test_NoParameters(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="There are no parameters"):
            self.supervisor.createCourse()
