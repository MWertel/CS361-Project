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

from CS361_Project.views import Login, Home, ManageAccounts, Notification, ManageCourse, ManageAssign, LogOut, \
    CreateCourse, EditCourse, DeleteCourse, CreateLab, EditLab, DeleteLab, CreateAccount, EditAccount, DeleteAccount, AssignUser,RemoveAssign,Profile, EditProfile

urlpatterns = [
    # Login is the home page -> ('')
    path('', Login.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('manage/', ManageAccounts.as_view(), name='manage_account'),
    path('manage/createAccount/', CreateAccount.as_view(), name='create_account'),
    path('manage/editAccount/', EditAccount.as_view(), name='edit_account'),
    path('manage/deleteAccount/', DeleteAccount.as_view(), name='delete_account'),

    path('assign/',ManageAssign.as_view(),name = 'manage_assign'),
    path('assign/assignUser/',AssignUser.as_view(), name = "assign_user"),
    path('assign/removeAssign/',RemoveAssign.as_view(), name = "remove_Assign"),

    path('notification/', Notification.as_view(), name="create_notification"),

    path('course/', ManageCourse.as_view(), name="course"),
    path('course/createCourse/', CreateCourse.as_view(), name='create_course'),
    path("course/editCourse/", EditCourse.as_view(), name = 'edit_course'),
    path("course/deleteCourse/", DeleteCourse.as_view(),name = "delete_course"),

    path('course/createLab/',CreateLab.as_view(), name = "create_lab"),
    path('course/editLab/',EditLab.as_view(), name = "edit_lab"),
    path('course/deleteLab/', DeleteLab.as_view(), name = 'delete_lab'),

    path('admin/', admin.site.urls),
    path('profile/', Profile.as_view(), name = "profile"),
    path('profile/edit', EditProfile.as_view(), name = "edit_profile"),
]
