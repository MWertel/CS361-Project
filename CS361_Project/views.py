from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor, Instructor, TA
import random as rand

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        try:
            user = Account.objects.get(username=Username)
        except:
            return render(request, "login.html", {"error": "User does not exist"})
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            return render(request, "login.html", {"error": "Incorrect Password"})


class Home(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'login'

    def get(self, request):
        return render(request, "Home.html")

    def post(self, request):
        pass

class SupCreateAccounts(LoginRequiredMixin, View):

    """
    def setName(self, other):
        self.account.name = other

    def setEmail(self, other):
        self.account.email = other
    """

    def generateID(self):

        #We assign ID in a first come, first serve method, checking all the existing IDs just to make sure that
        #none of the IDs are repeated
        accounts = list(Account.objects.all())
        idList = []

        for l in accounts:
            idList.append(l.id)

        #IDs are randomly assigned, should have way more numbers than expected users
        i = rand.randint(1,5000000)
        flag = True
        while(flag):
            if i not in idList:
                flag = False
            i += rand.randint(1,5000000)
        #Returns the unique ID (Cannot be done as a global variable that keep being added because an ID might be deleted=
        return i


    """
    def setRole(self, other):
        self.account.role = other

    def setPhoneNum(self, other):
        self.account.telephone = other

    def setAddress(self, other):
        self.account.telephone = other


    def setUsername(self, other):
        pass

    def setPassword(self,other):
        pass

    def saveAccount(self,other):
        pass 
    """


class SupEditAccounts(View):
    def __init__(self, account):
        self.account = account

    def changeName(self, change = "Null"):
        if type(change) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")


        if change == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.name = change
        self.account.save()

    def changeEmail(self, change = "Null"):
        if type(change) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if change == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.email = change
        self.account.save()

    def changeRole(self, change = "Null"):
        if type(change) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if change == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.role = change
        self.account.save()

    def changePhoneNum(self, change = "Null"):
        if type(change) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if change == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.telephone = change
        self.account.save()

    def changeAddress(self, other = "Null"):
        if type(other) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if other == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.address = other
        self.account.save()

    def changeUsername(self, other = "Null"):
        if type(other) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if other == "Null":
            raise ValueError("Null value fails raise ValueError")

        accounts = list(Account.objects.all())
        usernameList = []

        for i in accounts:
            usernameList.append(i.username)

        #if other is not within username list, make the change
        if other not in usernameList:
            self.account.username = other
            self.account.save()

    def changePassword(self,other = "Null"):
        if type(other) != str:
            raise TypeError("Name of Numbers fails to raise ValueError")

        if other == "Null":
            raise ValueError("Null value fails raise ValueError")

        self.account.password = other
        self.account.save()


