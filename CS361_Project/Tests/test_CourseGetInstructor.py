from django.test import TestCase
from CS361_Project.models import Course


class test_GetInstructor(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_GetInstructor(self):
        self.setUp()
        self.assertEqual("Soronson", self.rightArgs.getInstructor,
                         msg="Instructor should be \"Soronson\" was \"" + self.rightArgs.getInstructor() + "\"")
