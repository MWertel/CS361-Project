from django.test import TestCase, Client
from CS361_Project.models import Supervisor, Account, TA, Instructor

class DatabaseAccountTests(TestCase):
    user = None

    def setUp(self):
        account = Account(id=1, username="Steve", password="12345", role="Supervisor",name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor",name="james", email="james@uwm.edu", telephone="(+1)111-223-4334",address="3 Street")
        account.save()

    def testQuery(self):
        account1 = list(Account.objects.filter(id=1))
        account2 = list(Account.objects.filter(id=2))

        self.assertEqual(account1[0].username, "Steve")
        self.assertEqual(account2[0].username, "James")


class DatabaseSupervisortests(TestCase):
    user = None

    def setUp(self):
        account = Account(id=1, username="Steve", password="12345", role="Supervisor",name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",address="2 Street")
        supervisor = Supervisor(id=account)
        supervisor.save()
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor", name="james", email="james@uwm.edu", telephone="(+1)111-223-4334",address="3 Street")
        supervisor = Supervisor(id=account)
        supervisor.save()
        account.save()

    def testQuery(self):
        supervisor1 = list(Supervisor.objects.filter(id=1))
        supervisor2 = list(Supervisor.objects.filter(id=2))
        print(supervisor1)
        account1 = list(Account.objects.filter(id = supervisor1[0].id.id))
        account2 = list(Account.objects.filter(id=supervisor2[0].id.id))

        self.assertEqual(account1[0].email, "steve@uwm.edu")
        self.assertEqual(account2[0].email, "james@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id=1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the supervisor
        supervisor1 = list(Supervisor.objects.filter(id=1))
        self.assertEqual(len(supervisor1), 0)

        supervisor2 = list(Supervisor.objects.filter(id=2))
        self.assertEqual(len(supervisor2), 1)

class DatabaseInstructorTests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "James", password = "12345", role = "Instructor",name = "James",email = "james@uwm.edu",telephone = "(+1)111-222-3333",address = "2 Street")
        instructor = Instructor(id= account)
        account.save()
        instructor.save()


        account = Account(id=2, username="Michael", password="23456", role="Instructor", name="Michael", email="michael@uwm.edu", telephone="(+1)111-222-3333",address="2 Street")
        instructor = Instructor(id=account)

        account.save()
        instructor.save()

        account = Account(id=3, username="Steve", password="23456", role="Supervisor", name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",address="3 Street")
        supervisor = Supervisor(id=account)
        supervisor.save()
        account.save()

    def testQuery(self):
        #Check if the ID is in the instructor table
        instructor1 = list(Instructor.objects.filter(id = 1))
        instructor2 = list(Instructor.objects.filter(id = 2))

        #Get the values in the Account Table
        account1 = list(Account.objects.filter(id = instructor1[0].id.id))
        account2 = list(Account.objects.filter(id=instructor2[0].id.id))

        self.assertEqual(account1[0].email, "james@uwm.edu")
        self.assertEqual(account2[0].email, "michael@uwm.edu")

    def testDelete(self):
        Account.objects.filter(id = 1).delete()

        # Upon deleting the account which the ID is connected, the database should delete the TA
        instructor1 = list(Instructor.objects.filter(id = 1))
        self.assertEqual(len(instructor1),0)

        instructor2 = list(Instructor.objects.filter(id = 2))
        self.assertEqual(len(instructor2),1)

    def testAccountInstructorAccess(self):
        #The table should be able to pick from the Account, all those that are TA

        accounts = list(Account.objects.filter(role = "Instructor"))

        a1 = accounts[0]
        a2 = accounts[1]

        instructor1 = list(Instructor.objects.filter(id = a1.id))
        instructor2 = list(Instructor.objects.filter(id = a2.id))

        account1 = list(Account.objects.filter(id = instructor1[0].id.id))
        account2 = list(Account.objects.filter(id=instructor2[0].id.id))

        self.assertEqual(account1[0].name, "James")
        self.assertEqual(account2[0].name, "Michael")

class DatabaseTATests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "Eric", password = "12345", role = "TA",name = "Eric",email = "eric@uwm.edu",telephone = "(+1)111-222-3333",address = "2 Street")
        ta = TA(id= account)
        account.save()
        ta.save()


        account = Account(id=2, username="Kyle", password="23456", role="TA", name="Kyle", email="kyle@uwm.edu", telephone="(+1)111-222-3333",address="2 Street")
        ta = TA(id=account)

        account.save()
        ta.save()

        account = Account(id=3, username="Steve", password="23456", role="Supervisor", name="Steve", email="steve@uwm.edu", telephone="(+1)111-222-3333",address="3 Street")
        supervisor = Supervisor(id=account)
        supervisor.save()
        account.save()

    def testQuery(self):
        ta1 = list(TA.objects.filter(id = 1))
        ta2 = list(TA.objects.filter(id = 2))

        account1 = list(Account.objects.filter(id = ta1[0].id.id))
        account2 = list(Account.objects.filter(id=ta2[0].id.id))

        self.assertEqual(account1[0].email, "eric@uwm.edu")
        self.assertEqual(account2[0].email, "kyle@uwm.edu")

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

        ta1 = list(TA.objects.filter(id = a1))
        ta2 = list(TA.objects.filter(id = a2))



        self.assertEqual(ta1[0].id.id, a1.id)
        self.assertEqual(ta2[0].id.id,a2.id)