from django import forms

class SignInForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()