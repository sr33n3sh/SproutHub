from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from accounts.forms import *
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =form.save()
            return redirect('http://127.0.0.1:8000/clghome/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})
def college_register(request):
    if request.method == 'POST':
        form=college_Regform(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('http://127.0.0.1:8000/uploadlogo/')
    else:
        form=college_Regform()
    return render(request,'csignup.html',{'form':form})



def redi(request):
    return redirect('http://127.0.0.1:8000/clghome/')
