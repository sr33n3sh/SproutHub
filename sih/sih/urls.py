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
from sprouthub import views
from accounts import views as acc_views
urlpatterns = [
    path('', views.landingPage),
    path('admin/', admin.site.urls),
    path('search/',views.search,name='search'),
    #path('student_register/',views.student_register,name='student_register'),
    #path('college_register/',views.college_register,name='college_register'),
    # path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('student_register/',acc_views.signup),
    path('college_register/',acc_views.college_register),
    path('register/',views.register)
]
