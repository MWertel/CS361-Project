from django.test import TestCase
from CS361_Project.models import Course


class test_SetDepartment(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_SetDepartment(self):
        self.setUp()
        self.rightArgs.setDepartment("Math")
        self.assertEqual("Math", self.rightArgs.department, msg="Department should be Math was "
                                                                + self.rightArgs.department)

    def test_WrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.rightArgs.setDepartment(150)

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setDepartment("Math", "Art")

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setDepartment()
