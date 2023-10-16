from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import Avatar
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {"message": "Some of your information is incorrect"})
        else:
            return render(request, 'login.html', {"message": "ERROR, invalid form"})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return redirect('login')

    else:    
        form = UserRegisterForm()    

    return render(request,"signin.html" ,  {"form":form})

@login_required
def updateprofile(request):
    user = request.user

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()

            return render(request, "home.html")
        else:
            return render(request, "updateprofile.html", {"form": form, "Users": user})
    else:
        form = UserRegisterForm(
            initial={
                'email': user.email,
                'last_name': user.last_name,
                'first_name': user.first_name
            }
        )
    return render(request, "updateprofile.html", {"form": form, "Users": user})


@login_required
def update_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar.objects.get_or_create(user=request.user)[0]
            new_image = form.cleaned_data["image"]
            if new_image:
                avatar.image = new_image
                avatar.save()
            return redirect('profile')
    else:
        form = AvatarForm()
    return render(request, 'changeavatar.html', {'form': form})

class ChangePasswordView(LoginRequiredMixin, View):
    template_name = "changepass.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class})
    
    def post(self, request, *args, **kwargs):
        
        Users = User.objects.get(id=request.user.id)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            pass1 = form.cleaned_data.get("password1")
            pass2 = form.cleaned_data.get("password2")
        
            if pass1 == pass2:
                Users.set_password(pass1)
                Users.save()
                return redirect('home')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required           
def logout_request(request):
    logout(request)
    return render (request, 'logout.html')