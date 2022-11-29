from django.test import TestCase
from CS361_Project.models import Course


class test_GetCourseNum(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_GetCourseNum(self):
        self.setUp()
        self.assertTrue(self.rightArgs.getCourseNum() == 150,
                        msg="Course number should be \"150\" was \"" + self.rightArgs.getCourseNum() + "\"")
