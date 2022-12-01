from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import Account, Supervisor
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
