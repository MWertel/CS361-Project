from django.test import TestCase
from CS361_Project.models import Course


class test_SetCourseNum(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_SetCourseNum(self):
        self.setUp()
        self.rightArgs.setCourseNum(250)
        self.assertTrue(self.rightArgs.courseNum == 250,
                        msg="Course number should be \"250\" was \"" + self.rightArgs.courseNum + "\"")

    def test_WrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.rightArgs.setCourseNum("150")

    def test_NegativeCourseNumber(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be a positive number"):
            self.rightArgs.setCourseNum(-150)

    def test_TooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setCourseNum(250, 251)

    def test_TooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setCourseNum()
