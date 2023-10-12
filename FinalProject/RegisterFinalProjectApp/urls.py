from django.urls import path, include
from RegisterFinalProjectApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('signin', views.register, name="signin"),
    path('', include('BaseFinalProjectApp.urls')),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('updateuser', views.updateprofile, name="updateprofile"),
    path('changepass/', views.ChangePasswordView.as_view(), name="ChangePass"),
]