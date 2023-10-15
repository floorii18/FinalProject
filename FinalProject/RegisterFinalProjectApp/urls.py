from django.urls import path, include
from RegisterFinalProjectApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('signin', views.register, name="signin"),
    path('', include('BaseFinalProjectApp.urls')),
    path('logout', views.logout_request, name="logout"),
    path('updateuser', views.updateprofile, name="updateuser"),
    path('changepass', views.ChangePasswordView.as_view(), name="changepass"),
    path('profile', views.profile, name="profile"),
]