from django.test.client import RequestFactory
from django.test import TestCase


class testAuth(TestCase):
    rf = None

    def setUp(self):
        rf = RequestFactory()

    def testSuccess(self):
        get_request = self.rf.get('/')
        post_request = self.rf.post('/', {'user': 'admin', "password": 'admin'})

        post_request.session.get("user")["username"], post_request.POST.get("admin")
        post_request.session.get("user")["password"], post_request.POST.get("admin")

    def testFail(self):
        def testSuccess(self):
            get_request = self.rf.get('/')
            post_request = self.rf.post('/', {'user': 'admin', "password": 'wrong'})

            with self.assertRaises(ValueError, msg="Incorrect Password"):
                post_request.session.get("user")["username"], post_request.POST.get("admin")
                post_request.session.get("user")["password"], post_request.POST.get("admin")

    def test_NullUserName(self):
        def testSuccess(self):
            get_request = self.rf.get('/')
            post_request = self.rf.post('/', {'user': '', "password": 'admin'})

            with self.assertRaises(ValueError, msg="Username is missing"):
                post_request.session.get("user")["username"], post_request.POST.get("")

    def test_NullPassword(self):
        def testSuccess(self):
            get_request = self.rf.get('/')
            post_request = self.rf.post('/', {'user': 'admin', "password": ''})

            with self.assertRaises(ValueError, msg="Password is missing"):
                post_request.session.get("user")["password"], post_request.POST.get("")
