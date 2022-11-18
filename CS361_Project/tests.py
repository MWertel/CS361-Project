from django.test import TestCase, Client
from .models import Account, Supervisor


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

class DatabaseSupervisortests(TestCase):
    user = None
    def setUp(self):
        account = Account(id = 1, username = "Steve", password = "12345", role = "Supervisor")
        supervisor = Supervisor(id= account, name = "Steve",email = "steve@uwm.edu",telephone = "(+1)111-222-3333",
                                address = "2 Street")
        supervisor.save()
        account.save()

        account = Account(id=2, username="James", password="23456", role="Supervisor")
        supervisor = Supervisor(id= account, name="james", email="james@uwm.edu", telephone="(+1)111-223-4334",
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