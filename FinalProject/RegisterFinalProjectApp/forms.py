from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Insert your email:")
    last_name = forms.CharField()
    first_name = forms.CharField()
    avatar = forms.FileField()

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'avatar']
        help_text = {k: "" for k in fields}


class AvatarForm(forms.Form):
    avatar = forms.FileField()


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label="Insert again your password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Insert again your password", widget=forms.PasswordInput())
    