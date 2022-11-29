from django.test import TestCase
from CS361_Project.models import Course


class test_Str(TestCase):

    def setUp(self):
        self.course = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_Display(self):
        self.assertEqual("CompSci 150: Survey of Computer Science - Soronson", self.course.__str__(),
                         msg="String should be \"CompSci 150: Survey of Computer Science - Soronson\" was \""
                         + self.course.__str__() + "\"")
