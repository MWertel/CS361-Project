# Intention: easy verification and store a session on swift.
import ast

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
        return redirectSession(request)
    return render(request, 'login.html')


def redirectSession(request):
    context = {}
    print(request.session.has_key('context'))
    if request.session.has_key('context'):
        context.update({'context': request.session['context']})
    currentPath = request.path
    if currentPath == '/':
        return render(request, 'Home.html',context)
    return render(request, TemplatePath(currentPath),context)


def TemplatePath(path):
    cleanPath = path.replace('/', '')
    return cleanPath.capitalize() + '.html'


def hasSession(request):
    if not request.session.is_empty():
        return True
    return False


def errorRender(request, page: str, context: Exception):
    contextDict = ast.literal_eval(str(context))
    pageHTML = page + '.html'
    return render(request, pageHTML, contextDict)

