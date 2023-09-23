
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import college_Regform,student_Regform
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request,'home.html')

def search(request):
    return render(request,'search.html')

def student_register(request):
    name='student_register'
    form=student_Regform()
    if request.method == 'POST':
        form=student_Regform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, f'hi')
            return redirect('home')
    
    return render(request,'stu_ins.html',{'form':form,'name':name})


def college_register(request):
    name='college_register'
    form=college_Regform()
    if request.method == 'POST':
        form=college_Regform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, f'hi')
            return redirect('home')
    
    return render(request,'stu_ins.html',{'form':form,'name':name})

# def register(request):
#     # name='college_register'
#     form=Regform()
#     if request.method == 'POST':
#         form=Regform(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             messages.success(request, f'hi')
#             return redirect('home')
    
#     return render(request,'base/login_register.html',{'form':form})

def loginpage(request):
    page='login'
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form,'page':page})






def upload(request):
    return render(request,"checking.html")

def register(request):
    return render(request,"register.html")

def landingPage(request):
    return render(request,"landingPage.html",{"title":"LandingPage"})

def aboutPage(request):
    return render(request,"aboutPage.html",{"title":"aboutPage"})

from .models import Project 
def project_form(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        print("Posted")
        project_name = request.POST['project_name']
        description = request.POST['description']
        student_name = request.POST['student_name']
        student_email=request.POST['student_email']
        student_roll = request.POST['student_roll']
        project_file = request.FILES['project_file']
        project = Project(
            project_name=project_name,
            project_description=description,
            student_name=student_name,
            student_email=student_email,
            student_roll=student_roll,
            project_file=project_file
        )
        project.save()
    return render(request, 'clg_home.html',{'projects': projects})
