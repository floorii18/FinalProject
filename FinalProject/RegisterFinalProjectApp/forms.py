from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        help_text=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        help_text=''
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text=''
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text=''
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
        
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Insert your email:")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repit Password', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["image"]


class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(label="Insert again your password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Insert again your password", widget=forms.PasswordInput())
    