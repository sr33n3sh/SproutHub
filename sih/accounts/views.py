from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from accounts.forms import *
from sprouthub.forms import college_Regform
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})
def college_register(request):
    if request.method == 'POST':
        form=college_Regform(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form=college_Regform()
    return render(request,'csignup.html',{'form':form})

def uploadProject(request):
    name='upload'
    form = project()
    if request.method == 'POST':
        form= project(request.POST)
