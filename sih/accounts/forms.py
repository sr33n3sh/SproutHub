from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    studentid=forms.CharField(required=True,widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'studentid','password1','password2')

class college_Regform(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    collegeid=forms.CharField(required=True,widget=forms.TextInput())
    location = forms.CharField(max_length=200,required=True,widget=forms.TextInput())

    class Meta:
        model = User
        fields=('username','email','location','password1','password2')