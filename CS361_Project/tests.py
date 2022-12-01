from django.test import TestCase, Client
from .models import Account, Supervisor, Instructor, TA


class DatabaseAccountTests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "Steve", password = "12345", role = "Supervisor")
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor")
        account.save()
    def testQuery(self):
        account1 = list(Account.objects.filter(id = 1))
        account2 = list(Account.objects.filter(id = 2))

        self.assertEqual(account1[0].username, "Steve")
        self.assertEqual(account2[0].username, "James")

    def testUniqueID(self):

        #There cannot be two ID one's so it should overwrite the original
        account = Account(id = 1, username = "Jonas", password = "54321", role = "Supervisor")
        account.save()

        account1 = list(Account.objects.filter(id=1))

        self.assertEqual(account1[0].username, "Jonas")




class DatabaseSupervisorTests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "Steve", password = "12345", role = "Supervisor")
        supervisor = Supervisor(id= account, name = "Steve",email = "steve@uwm.edu",telephone = "(+1)111-222-3333",
                                address = "2 Street")
        supervisor.save()
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor")
        supervisor = Supervisor(id= account, name="James", email="james@uwm.edu", telephone="(+1)111-223-4334",
                                address="3 Street")
        supervisor.save()
        account.save()

    def testQuery(self):
        supervisor1 = list(Supervisor.objects.filter(id = 1))
        supervisor2 = list(Supervisor.objects.filter(id = 2))

        self.assertEqual(supervisor1[0].email, "steve@uwm.edu")
        self.assertEqual(supervisor2[0].email, "james@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id = 1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the supervisor
        supervisor1 = list(Supervisor.objects.filter(id = 1))
        self.assertEqual(len(supervisor1),0)

        supervisor2 = list(Supervisor.objects.filter(id = 2))
        self.assertEqual(len(supervisor2),1)


class DatabaseInstructorTests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "James", password = "12345", role = "Instructor")
        instructor = Instructor(id= account, name = "James",email = "james@uwm.edu",telephone = "(+1)111-222-3333",

                                address = "2 Street")
        account.save()
        instructor.save()


        account = Account(id=2, username="Michael", password="23456", role="Instructor")
        instructor = Instructor(id=account, name="Michael", email="kyle@uwm.edu", telephone="(+1)111-222-3333",
                address="2 Street")

        account.save()
        instructor.save()

        account = Account(id=3, username="Steve", password="23456", role="Supervisor")
        supervisor = Supervisor(id=account, name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",
                address="3 Street")
        supervisor.save()
        account.save()

    def testQuery(self):
        instructor1 = list(Instructor.objects.filter(id = 1))
        instructor2 = list(Instructor.objects.filter(id = 2))

        self.assertEqual(instructor1[0].email, "james@uwm.edu")
        self.assertEqual(instructor2[0].email, "michael@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id = 1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the TA
        instructor1 = list(Instructor.objects.filter(id = 1))
        self.assertEqual(len(instructor1),0)

        instructor2 = list(Instructor.objects.filter(id = 2))
        self.assertEqual(len(instructor2),1)

    def testAccountInstructorAccess(self):
        #The table should be able to pick from the Account, all those that are TA

        accounts = list(Account.objects.filter(role = "Intructor"))

        a1 = accounts[0]
        a2 = accounts[1]

        instructor1 = list(Instructor.objects.filter(id = a1.id))
        instructor2 = list(Instructor.objects.filter(id = a2.id))

        self.assertEqual(instructor2[0].name, "Eric")
        self.assertEqual(instructor2[0].name, "Kyle")

class DatabaseTATests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "Eric", password = "12345", role = "TA")
        ta = TA(id= account, name = "Eric",email = "eric@uwm.edu",telephone = "(+1)111-222-3333",

                                address = "2 Street")
        account.save()
        ta.save()


        account = Account(id=2, username="Kyle", password="23456", role="TA")
        ta = TA(id=account, name="Kyle", email="kyle@uwm.edu", telephone="(+1)111-222-3333",
                address="2 Street")

        account.save()
        ta.save()

        account = Account(id=3, username="Steve", password="23456", role="Supervisor")
        supervisor = Supervisor(id=account, name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",
                address="3 Street")
        supervisor.save()
        account.save()

    def testQuery(self):
        ta1 = list(TA.objects.filter(id = 1))
        ta2 = list(TA.objects.filter(id = 2))

        self.assertEqual(ta1[0].email, "eric@uwm.edu")
        self.assertEqual(ta2[0].email, "kyle@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id = 1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the TA
        ta1 = list(TA.objects.filter(id = 1))
        self.assertEqual(len(ta1),0)

        ta2 = list(TA.objects.filter(id = 2))
        self.assertEqual(len(ta2),1)

    def testAccountTAAccess(self):
        #The table should be able to pick from the Account, all those that are TA

        accounts = list(Account.objects.filter(role = "TA"))

        a1 = accounts[0]
        a2 = accounts[1]

        ta1 = list(TA.objects.filter(id = a1.id))
        ta2 = list(TA.objects.filter(id = a2.id))

        self.assertEqual(ta1[0].name, "Eric")
        self.assertEqual(ta2[0].name, "Kyle")