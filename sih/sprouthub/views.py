
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










def register(request):
    return render(request,"register.html")

def landingPage(request):
    return render(request,"landingPage.html",{"title":"LandingPage"})
