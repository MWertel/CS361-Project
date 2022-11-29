from django.test import TestCase
from CS361_Project.models import Course


class test_GetCourseName(TestCase):

    def setUp(self):
        self.course = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_GetCourseName(self):
        self.setUp()
        self.assertEqual("Survey of Computer Science", self.course.name,
                         msg="Course name should be \"Survey of Computer Science\" was \"" + self.course.name + "\"")
