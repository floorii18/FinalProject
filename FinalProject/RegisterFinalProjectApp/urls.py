from django.urls import path, include
from RegisterFinalProjectApp import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signin', views.signin, name="signin"),
    path('', include('BaseFinalProjectApp.urls')),
]