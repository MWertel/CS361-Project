from django.test import TestCase, Client
from CS361_Project.views import SupCreateAccounts
from CS361_Project.views import SupEditAccounts
from django.test import TestCase, Client
from CS361_Project.models import Account, Supervisor


# Tests for Supervisor Creating Accounts


class SupCreateAccount(TestCase):

    def setUp(self):
        self.manage = SupCreateAccounts()


    def testIDGeneration(self):
        newId = self.manage.generateID()
        #the first ID created ever, must be one
        self.assertEqual(1,newId)
        #new accounts is created
        account = Account(id = newId, username = "Steve", password = "SteveMaximus", role = "Supervisor")
        account.save()

        oldId = newId

        newId = self.manage.generateID()
        #The second id, simply, should not be equal to the old id
        self.assertNotEqual(newId,oldId)

    """
    def testNullName(self):

        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            self.accountCreate.setName()

    def testInvalidName(self):
        with self.assertRaises(TypeError, msg="Name of numbers fails to raise ValueError"):
            self.accountCreate.setName(1)

    def testSetEmail(self):
        self.accountCreate.setEmail("john.doe@uwm.edu")
        self.assertEqual("john.doe@uwm.edu", self.accountCreate.account.email)

    def testSetID(self):
        a = SupCreateAccounts("John Doe")
        self.assertEqual(1, a.setID(1))

    def testSetRole(self):
        self.accountCreate.setRole("Instructor")
        self.assertEqual("Instructor", self.accountCreate.account.role)

    def testSetPhone(self):
        self.accountCreate.setPhoneNum("5558675309")
        self.assertEqual("5558675309", self.accountCreate.account.telephone)

    def testSetAddress(self):
        self.accountCreate.setAddress("1234 test ave.")
        self.assertEqual("1234 test ave.", self.accountCreate.account.address)

    def testSetUsername(self):
        self.accountCreate.setUsername("JohnD")

    # Tests for Supervisor editing Accounts
"""

class SupEditAccount(TestCase):

    def setUp(self):
        self.account = Account(id=2, username="JohnD", password="12345", role="Supervisor", name="John",
                               email="john.deo@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        self.account.save()

        self.account2 = Account(id=1, username="JoshB", password="12345", role="Instructor", name="Josh",
                               email="josh.bideo@uwm.edu", telephone="(+1)111-222-3333", address="2 Street")
        self.account2.save()

    def testNullName(self):
        a = SupEditAccounts(self.account)
        with self.assertRaises(ValueError, msg="Null value fails raise ValueError"):
            a.changeName()

    def testInvalidName(self):
        a = SupEditAccounts(self.account)
        with self.assertRaises(TypeError, msg="Name of Numbers fails to raise ValueError"):
            a.changeName(123)

    def testChangeEmail(self):
        a = SupEditAccounts(self.account)
        a.changeEmail("john.doe@uwm.edu")
        self.assertEqual("john.doe@uwm.edu", self.account.email)

    def testChangeRole(self):
        a = SupEditAccounts(self.account)
        a.changeRole("Instructor")
        self.assertEqual("Instructor", self.account.role)

    def testChangePhone(self):
        a = SupEditAccounts(self.account)
        a.changePhoneNum("5558675309")
        self.assertEqual("5558675309", self.account.telephone)

    def testChangeAddress(self):
        a = SupEditAccounts(self.account)
        a.changeAddress("1234 test ave.")
        self.assertEqual("1234 test ave.", self.account.address)

    def testChangePassword(self):
        a = SupEditAccounts(self.account)
        a.changePassword("New Password")
        self.assertEqual("New Password",self.account.password)

    def testInvalidPassword(self):
        a = SupEditAccounts(self.account)
        with self.assertRaises(TypeError, msg="Name of Numbers fails to raise ValueError"):
            a.changePassword(v = [])

    def testChangeUsername(self):
        a = SupEditAccounts(self.account)
        a.changeUsername("New Username")
        self.assertEqual("New Username",self.account.username)

    def testRepeatedUsername(self):
        a = SupEditAccounts(self.account2)
        a.changeUsername("JohnD")#Should not be able to change, therefore the change should happen
        self.assertNotEqual("JohnD",self.account2.username)
