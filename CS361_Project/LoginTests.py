from django.test import TestCase, Client
from .models import Account, Supervisor, Instructor, TA


class DefaultLoginTests(TestCase):

    def setUp(self):
        AdminAccount = Account(id=1, username="Dan", password="123456", role="Supervisor")
        SupervisorAccount = Supervisor(id=AdminAccount, name='Dan', email='danhcle@uwm.edu',
                                       telephone='(+1)414-526-4865',
                                       address="123 BLVD")
        AdminAccount.save()
        SupervisorAccount.save()

    def testFailedLogin(self):
        client = Client()
        response = client.post('/', {'username': 'Dan', 'password': '123'})
        message = response.context['error']
        self.assertEqual('Incorrect password', message)

    def testDoesNotExist(self):
        client = Client()
        response = client.post('/', {'username': 'hey', 'password': '123456'})
        message = response.context['error']
        self.assertEqual('User does not exist', message)
