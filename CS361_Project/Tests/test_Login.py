from django.test import TestCase, Client
from django.contrib.auth.models import User
from CS361_Project.models import Account, Supervisor, Instructor, TA


class DefaultLoginTests(TestCase):

    def setUp(self):
        account = Account(id=1, username="Dan", password="123456", role="Supervisor", name="Dan Le",
                          email="danhcle@uwm.edu", telephone="111-111-111",
                          address="123 Street")
        account.save()

        user = User.objects.create(username="Dan")
        user.set_password("123456")
        user.save()

    # Normal client's Post request.
    def testDoesNotExist(self):
        client = Client()
        response = client.post('/', {'username': 'hey', 'password': '123456'})
        message = response.context['error']
        self.assertEqual('User does not exist', message)

    def testIncorrectPasswordMessage(self):
        client = Client()
        response = client.post('/', {'username': 'Dan', 'password': "12345"})
        message = response.context['error']
        self.assertEqual("Incorrect Password", message)

    # Usage of login() from Django Authentication -> Required dummy account.
    def testFailedLogin(self):
        client = Client()
        logIn = client.login(username="Dan", password="123")
        # Log in failed due to incorrect password.
        self.assertFalse(logIn)

    def testSuccessLogin(self):
        client = Client()
        response = client.get('/home', follow=True)
        last_url, status_code = response.redirect_chain[-1]

        # Previous page. (This page required a person to log in to view /home)
        self.assertURLEqual('/?login=/home/', last_url)
        # Successful logged in returned 302
        self.assertEqual(302, status_code)

        # After login current page is /home.
        logIn = client.login(username="Dan", password="123456")
        # Logged in success with correct password and username
        self.assertTrue(logIn)

        response = client.get('/home', follow=True)
        last_url, status_code = response.redirect_chain[-1]

        # Status Code 301 = Permanent Redirection occurred.
        self.assertEqual(301, status_code)
        # Current page. There isn't any "previous" page.
        self.assertURLEqual('/home/', last_url)
