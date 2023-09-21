from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class student_Regform(UserCreationForm):
    email = forms.EmailField(required=True)
    institution=forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ("username","institution", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(student_Regform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class college_Regform(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile=forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ("username","mobile", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(college_Regform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user