from django.test import TestCase
from CS361_Project.models import Course


class test_SetName(TestCase):

    def setUp(self):
        self.course = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_SetName(self):
        self.setUp()
        self.course.setName("System Programming")
        self.assertEqual("System Programming", self.course.name,
                         msg="Course name should be \"System Programming\" was \"" + self.course.name + "\"")

    def test_WrongArgType(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course name should be a string"):
            self.course.setName(25)

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.course.setName("System Programming", "Computer Architecture")

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.course.setName()
