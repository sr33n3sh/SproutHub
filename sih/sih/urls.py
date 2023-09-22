"""
URL configuration for sih project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from sprouthub import views
from accounts import views as acc_views
urlpatterns = [
    path('', views.landingPage, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('search/',views.search,name='search'),
    path('student_register/',acc_views.signup),
    path('college_register/',acc_views.college_register),
    path('register/',views.register),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'), 
    path('accounts/profile/',acc_views.redi),
    path('list/',views.project_form, name='project_form'),
    path('clghome/', views.project_list, name='project_list'),
    path('about/',views.aboutPage, name='about_page'),
]
