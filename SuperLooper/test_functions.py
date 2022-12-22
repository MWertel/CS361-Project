from SuperLooper import functions
import unittest


class TestFunctions(unittest.TestCase):

    def test_generateID(self):
        thislist = []

        for x in range(10):
            thislist.append(functions.generateID())

        for x in thislist:
            if x < 0:
                self.assertRaises(ValueError, msg="Negative ID")

    def test_changeNameNumber(self):
        with self.assertRaises(TypeError, msg="Name Not a String"):
            functions.changeName(4)

    def test_changeNameNull(self):
        with self.assertRaises(ValueError, msg="Null Name Change"):
            functions.changeName("")

    def test_changeEmailNumber(self):
        with self.assertRaises(TypeError, msg="Email Not a String"):
            functions.changeEmail(4)

    def test_changeEmailNull(self):
        with self.assertRaises(ValueError, msg="Null Email Change"):
            functions.changeEmail("")

    def test_changeRoleNumber(self):
        with self.assertRaises(TypeError, msg="Role Not a String"):
            functions.changeRole(4)

    def test_changeRoleNull(self):
        with self.assertRaises(ValueError, msg="Null Role Change"):
            functions.changeRole("")

    def test_changeTelephoneNumber(self):
        with self.assertRaises(TypeError, msg="Telephone Not a String"):
            functions.changeRole(4)

    def test_changeTelephoneNull(self):
        with self.assertRaises(ValueError, msg="Null Telephone Change"):
            functions.changeRole("")

    def test_changeAddressNumber(self):
        with self.assertRaises(TypeError, msg="Address Not a String"):
            functions.changeRole(4)

    def test_changeAddressNull(self):
        with self.assertRaises(ValueError, msg="Null Address Change"):
            functions.changeRole("")
