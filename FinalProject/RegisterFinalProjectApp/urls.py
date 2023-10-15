from django.urls import path, include
from RegisterFinalProjectApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('signin', views.register, name="signin"),
    path('', include('BaseFinalProjectApp.urls')),
    path('logout', views.logout, name="logout"),
    path('updateuser', views.updateprofile, name="updateuser"),
    path('changepass', views.ChangePasswordView.as_view(), name="changepass"),
     path('logout/', LogoutView.as_view(template_name='RegisterFinalProjectApp/templates/logout.html'), name="logout"),
    path('profile', views.profile, name="profile"),
]