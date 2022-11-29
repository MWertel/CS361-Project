from django.test import TestCase, Client
from .models import Account, Supervisor, Course


class DatabaseAccountTests(TestCase):
    user = None

    def setUp(self):
        account = Account(id=1, username="Steve", password="12345", role="Supervisor")
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor")
        account.save()

    def testQuery(self):
        account1 = list(Account.objects.filter(id=1))
        account2 = list(Account.objects.filter(id=2))

        self.assertEqual(account1[0].username, "Steve")
        self.assertEqual(account2[0].username, "James")


class DatabaseSupervisortests(TestCase):
    user = None

    def setUp(self):
        account = Account(id=1, username="Steve", password="12345", role="Supervisor")
        supervisor = Supervisor(id=account, name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",
                                address="2 Street")
        supervisor.save()
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor")
        supervisor = Supervisor(id=account, name="james", email="james@uwm.edu", telephone="(+1)111-223-4334",
                                address="3 Street")
        supervisor.save()
        account.save()

    def testQuery(self):
        supervisor1 = list(Supervisor.objects.filter(id=1))
        supervisor2 = list(Supervisor.objects.filter(id=2))

        self.assertEqual(supervisor1[0].email, "steve@uwm.edu")
        self.assertEqual(supervisor2[0].email, "james@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id=1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the supervisor
        supervisor1 = list(Supervisor.objects.filter(id=1))
        self.assertEqual(len(supervisor1), 0)

        supervisor2 = list(Supervisor.objects.filter(id=2))
        self.assertEqual(len(supervisor2), 1)


class testCourse(TestCase):

    def setUp(self):
        self.rightArgs = Course("CompSci", 150, "Survey of Computer Science", "Soronson")

    def test_init(self):
        self.setUp()
        self.assertEqual("CompSci", self.rightArgs.department, msg="Department should be CompSci was " + self.rightArgs.department)
        self.assertTrue(self.rightArgs.courseNum == 150, msg="Course Number should be 150 was " + self.rightArgs.courseNum)
        self.assertEqual("Survey of Computer Science", self.rightArgs.name, msg="Course name should be Survey of "
                                                                                "Computer Science was " +
                                                                                self.rightArgs.name)
        self.assertEqual("Soronson", self.rightArgs.instructor, msg="Instructor should be Soronson was " + self.rightArgs.instructor)

    def test_initWrongArgs(self):
        with self.assertRaises(TypeError, msg="Department name should be a string"):
            a = Course(27, 150, "Survey of Computer Science", "Soronson")

        with self.assertRaises(TypeError, msg="Course Number should be an integer"):
            b = Course("CompSci", "150", "Survey of Computer Science", "Soronson")

        with self.assertRaises(TypeError, msg="Course Number should be positive"):
            c = Course("CompSci", -150, "Survey of Cpmuter Science", "Soronson")

        with self.assertRaises(TypeError, msg="Course name should be a string"):
            d = Course("CompSci", 150, 45, "Soronson")

        with self.assertRaises(TypeError, msg="Instructor should be a string"):
            e = Course("CompSci", 150, "Survey of Computer Science", 35)

    def test_initTooManyArgs(self):
        with self.assertRaises(TypeError, msg="Too many arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science", "Soronson", 1300)

    def test_initTooLittleArgs(self):
        with self.assertRaises(TypeError, msg="Too little arguments"):
            a = Course("CompSci", 150, "Survey of Computer Science")

    def test_SetName(self):
        self.setUp()
        self.rightArgs.setName("System Programming")
        self.assertEqual("System Programming", self.rightArgs.name, msg="Course name should be System Programming was + " + self.rightArgs.name)

    def test_SetNameWrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course Name should be a string"):
            self.rightArgs.setName(150)

    def test_SetNameTooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setName("System Programming", "Computer Architecture")

    def test_SetNameTooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setName()

    def test_GetName(self):
        self.setUp()
        self.assertEqual("Survey of Computer Science", self.rightArgs.getName(), msg="Course name should be Survey of "
                                                                                     "computer Science was " +
                                                                                     self.rightArgs.getName())

    def test_SetInstructor(self):
        self.setUp()
        self.rightArgs.setInstructor("Bacon")
        self.assertEqual("Bacon", self.rightArgs.instructor, msg="Instructor should be Bacon was " + self.rightArgs.instructor)

    def test_SetInstructorWrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Instructor should be a string"):
            self.rightArgs.setInstructor(100)

    def test_SetInstructorTooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setInstructor("Bacon", "Bourne")

    def test_SetInstructorTooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setInstructor()

    def test_GetInstructor(self):
        self.setUp()
        self.assertEqual("Soronson", self.rightArgs.getInstructor, msg="Instructor should be Soronson was " + self.rightArgs.getInstructor())

    def test_GetDepartment(self):
        self.setUp()
        self.assertEqual("CompSci", self.rightArgs.getDepartment, msg="Department should be CompSci was " + self.rightArgs.getDepartment())

    def test_SetDepartment(self):
        self.setUp()
        self.rightArgs.setDepartment("Math")
        self.assertEqual("Math", self.rightArgs.department, msg="Department should be Math was " + self.rightArgs.department)

    def test_SetDepartmentWrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Department should be a string"):
            self.rightArgs.setDepartment(150)

    def test_SetDepartmentTooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setDepartment("Math", "Art")

    def test_SetDepartmentTooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setDepartment()

    def test_GetCourseNum(self):
        self.setUp()
        self.assertTrue(self.rightArgs.getCourseNum() == 150, msg="Course number should be 150 was " + self.rightArgs.getCourseNum())

    def test_SetCourseNum(self):
        self.setUp()
        self.rightArgs.setCourseNum(250)
        self.assertTrue(self.rightArgs.courseNum == 250, msg="Course number should be 250 was " + self.rightArgs.courseNum)

    def test_SetCourseNumWrongArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be an integer"):
            self.rightArgs.setCourseNum("150")

    def test_SetCourseNumNegNumber(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Course number should be a positive number"):
            self.rightArgs.setCourseNum(-150)

    def test_SetCourseNumTooManyArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Too many arguments"):
            self.rightArgs.setCourseNum(250, 251)

    def test_SetCourseNumTooLittleArgs(self):
        self.setUp()
        with self.assertRaises(TypeError, msg="Not enough arguments"):
            self.rightArgs.setCourseNum()


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

