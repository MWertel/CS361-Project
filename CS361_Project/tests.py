import unittest

from views import SupCreateAccounts
from views import SupEditAccounts
from django.test import TestCase, Client
from .models import Account, Supervisor


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

    # Tests for Supervisor Creating Accounts


class SupCreateAccount(unittest.TestCase):
    def testNullName(self):
        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            a = SupCreateAccounts.setName();

    def testInvalidName(self):
        with self.assertRaises(TypeError, msg="Name of letters fails to raise ValueError"):
            a = SupCreateAccounts.setName(1, "test")

    def testSetEmail(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual(a.setEmail("john.doe@uwm.edu"))

    def testSetID(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual(a.setID("John Doe", 1))

    def testSetRole(self):
        a = SupCreateAccounts("John Doe", "instructor")
        self.assertEqual(a.setRole("John Doe", "Instructor"))

    def testSetPhone(self):
        a = SupCreateAccounts("John Doe", 5558675309)
        self.assertEqual(a.setPhoneNum("John Doe", 5558675309))

    def testSetAddress(self):
        a = SupCreateAccounts("John Doe", "1234 test ave.")
        self.assertEqual(a.setAddress("John Doe", "1234 test ave."))

    # Tests for Supervisor editing Accounts
class SupEditAccount(unittest.TestCase):

    def testNullName(self):
        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            a = SupEditAccounts.changeName();

    def testInvalidName(self):
        with self.assertRaises(TypeError, msg="Name of letters fails to raise ValueError"):
            a = SupEditAccounts.changeName("John Doe", 123);

    def testChangeEmail(self):
        a = SupEditAccounts("John Doe")
        self.assertEqual(a.changeEmail("john.deo@uwm.edu", "john.doe@uwm.edu"))

    def testChangeID(self):
        a = SupEditAccounts("John Doe")
        self.assertEqual(a.changeID(2, 1))

    def testChangeRole(self):
        a = SupEditAccounts("John Doe", "instructor")
        self.assertEqual(a.changeRole("TA", "Instructor"))

    def testChangePhone(self):
        a = SupEditAccounts("John Doe", 5558675309)
        self.assertEqual(a.changePhoneNum(5551234567, 5558675309))

    def testChangeAddress(self):
        a = SupEditAccounts("John Doe", "1234 test ave.")
        self.assertEqual(a.changeAddress("change me", "1234 test ave."))
