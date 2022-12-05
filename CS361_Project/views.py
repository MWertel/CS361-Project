from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor, Instructor, TA

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

class SupCreateAccounts(View):

    def __init__(self, name):
        pass

    def setName(self, other):
        pass

    def setEmail(self, other):
        pass

    def setID(self, other):
        pass

    def setRole(self, other):
        pass

    def setPhoneNum(self, other):
        pass

    def setAddress(self, other):
        pass


class SupEditAccounts(View):
    def __init__(self, account):
        pass

    def changeName(self, other, change):
        pass

    def changeEmail(self, other, change):
        pass

    def changeID(self, other, change):
        pass

    def changeRole(self, other, change):
        pass

    def changePhoneNum(self, other, change):
        pass

    def changeAddress(self, other):
        pass
