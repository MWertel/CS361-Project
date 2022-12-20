# Intention: easy verification and store a session on swift.
from django.shortcuts import redirect, render
from CS361_Project.models import Account
from SuperLooper.modelDict import Account_Dict


def login(request):
    context = {}
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == '' or password == '':
        if username == '':
            context = {'error': 'Username is missing'}
        if password == '':
            context = {'error': 'Password is missing'}
        if password == '' and username == '':
            context = {'error': "Username and Password is missing"}
        raise ValueError(context)
    try:
        user = Account.objects.get(username=username)
    except:
        context = {"error": "User does not exist"}
        raise ValueError(context)

    if user.password != password:
        context = {'error': 'Incorrect Password'}
        raise ValueError(context)

    request.session['user'] = Account_Dict(user)
    request.session['is_authenticate'] = True
    return request.session


def checkAuthentication(request):
    if hasSession(request):
        redirectSession(request)
    return render(request, 'login.html')


def redirectSession(request):
    currentPath = request.path
    if hasSession(request) and currentPath == '/':
        return redirect('/home')
    return redirect(currentPath)


def hasSession(request):
    if request.session.is_empty() or not request.session['is_authenticate']:
        return False
    return True
