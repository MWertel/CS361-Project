import unittest

from CS361_Project.views import SupCreateAccounts
from CS361_Project.views import SupEditAccounts
from django.test import TestCase, Client
from CS361_Project.models import Account, Supervisor


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
