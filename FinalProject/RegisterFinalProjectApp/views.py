from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request,'home.html', {"message":f"Welcome"})
            else:
                return render(request, 'login.html', {"message":f"Some of your information is incorrect"})
        else:
            return render(request, 'login.html', {"message":f"ERROR, invalid form"})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"home.html" ,  {"message":"User created succesfully"})

    else:    
        form = UserRegisterForm()    

    return render(request,"signin.html" ,  {"form":form})

@login_required
def updateprofile(request):

    Users = request.user

    if request.method == 'POST':

        form = MyUserEditForm(request.POST, request.FILES)

        if form.is_valid():
            
            information = form.cleaned_data
            Users.email = information['email']
            Users.password1 = information['password1']
            Users.password2 = information['password2']
            Users.last_name = information['last_name']
            Users.first_name = information['first_name']
            Users.save()

            form.save()
            # perfil.avatar = archivo_form.cleaned_data["avatar"]
            #perfil.save()

            user = User.objects.get(username=request.user)
            avat = Avatar.objects.get(user=user)
            print(f"\n\n{form.cleaned_data}\n\n")
            avat.image = form.cleaned_data["avatar"]
            print(f"\n\n{avat.image.url}\n\n")
            print(f"\n\n{avat.image.path}\n\n")
            # avatar = Avatar(user=user, imagen=archivo_form.cleaned_data["avatar"])
            avat.save()

            # archivo_form.save()


            return render(request, "AppCoder/index.html")
        else:
            form = MyUserEditForm()

    else:
        form = MyUserEditForm(
            initial={
                'email': Users.email,
                'last_name': Users.last_name,
                'first_name': Users.first_name
            }
        )
    return render(
        request,
        "users/updateprofile.html",
        {
            "form": form,
            "Users": Users
        }
    )

class ChangePasswordView(LoginRequiredMixin, View):
    template_name = "cambiar_pass.html"
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
                return render(request, "home.html")