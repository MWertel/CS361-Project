from django.test import TestCase, Client
from CS361_Project.models import Supervisor, Account

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
