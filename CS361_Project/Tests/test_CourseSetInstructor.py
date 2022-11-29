from django.test import TestCase
from CS361_Project.models import Course


class test_SetInstructor(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_SetInstructor(self):
        self.setUp()
        self.rightArgs.setInstructor("Bacon")
        self.assertEqual("Bacon", self.rightArgs.instructor, msg="Instructor should be Bacon was "
                                                                 + self.rightArgs.instructor)

    def test_WrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Instructor should be a string"):
            self.rightArgs.setInstructor(100)

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setInstructor("Bacon", "Bourne")

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setInstructor()

