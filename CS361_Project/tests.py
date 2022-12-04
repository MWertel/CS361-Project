import unittest

from .views import SupCreateAccounts
from .views import SupEditAccounts
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


class DatabaseSupervisorTests(TestCase):
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
            a = SupCreateAccounts(" ")
            a.setName(" ")

    def testInvalidName(self):
        with self.assertRaises(TypeError, msg="Name of numbers fails to raise ValueError"):
            a = SupCreateAccounts(1)
            a.setName(1)

    def testSetEmail(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual("john.doe@uwm.edu", a.setEmail("john.doe@uwm.edu"))

    def testSetID(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual(1, a.setID(1))

    def testSetRole(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual("Instructor", a.setRole("Instructor"))

    def testSetPhone(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual("5558675309", a.setPhoneNum(5558675309))

    def testSetAddress(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual("1234 test ave.", a.setAddress("1234 test ave."))

    # Tests for Supervisor editing Accounts


class SupEditAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(id=2, username="JohnD", password="12345", role="Supervisor", name="John",
                          email="john.deo@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        self.account.save()

    def testNullName(self):
        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            a = SupEditAccounts.changeName();

    def testInvalidName(self):
        with self.assertRaises(TypeError, msg="Name of Numbers fails to raise ValueError"):
            a = SupEditAccounts.changeName("John Doe", 123);

    def testChangeEmail(self):
        a = SupEditAccounts(self.account)
        self.assertEqual("john.doe@uwm.edu", a.changeEmail("john.doe@uwm.edu"))

    def testChangeID(self):
        a = SupEditAccounts(self.account)
        self.assertEqual(1, a.changeID(1))

    def testChangeRole(self):
        a = SupEditAccounts(self.account)
        self.assertEqual("Instructor", a.changeRole("Instructor"))

    def testChangePhone(self):
        a = SupEditAccounts(self.account)
        self.assertEqual(5558675309, a.changePhoneNum(5558675309))

    def testChangeAddress(self):
        a = SupEditAccounts(self.account)
        self.assertEqual("1234 test ave.", a.changeAddress("1234 test ave."))
