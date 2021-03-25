from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserRegisterForm

class UserRegisterForm(UserRegisterForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        