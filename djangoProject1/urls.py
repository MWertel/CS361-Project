"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from CS361_Project.views import Login, Home, ManageAccounts, Notification, ManageCourse, Assigns, Database, LogOut, \
    CreateAccount

urlpatterns = [
    # Login is the home page -> ('')
    path('', Login.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('manage/', ManageAccounts.as_view(), name='manage_account'),
    path('manage/createAccount/', CreateAccount.as_view(), name='create_account'),
    path('notification/', Notification.as_view(), name="create_notification"),
    path('course/', ManageCourse.as_view(), name="course"),
    path('assign/', Assigns.as_view(), name="assign_person"),
    path('data/', Database.as_view(), name="view_data"),
    path('admin/', admin.site.urls),
]
