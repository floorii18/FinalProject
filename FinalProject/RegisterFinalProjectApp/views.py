from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignInForm

def signin(request):
    return render(request,'signin.html')

def login(request):
    return render(request,'login.html')

def Register_newaccout(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request,'', {"message":f"Welcome"})
            else:
                return render(request, 'login.html', {"message":f"Some of your information in wrong"})
        else:
            return render(request, '', {"message":f"ERROR, invalid form"})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})