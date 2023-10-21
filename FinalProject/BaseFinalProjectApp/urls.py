from django.urls import path
from BaseFinalProjectApp import views
from .views import *

urlpatterns = [
    path('', views.Home, name=""),
    path('home/', views.Home, name="home"),
    path('experience/', views.Experience, name="experience"),
    path('certifications/', views.Certifications, name="certifications"),
    path('addcertification/', views.AddCertification, name='addcertification'),
    path('deletecertification/<int:pk>/', views.DeleteCertification, name='deletecertification'),
    path('updatecertification/<int:pk>/', views.UpdateCertification, name='updatecertification'),
    path('skills/', views.Skill, name="skills"),
    path('addsoftskills/', views.addsoftskill, name="addsoftskills"),
    path('addhardskills/', views.addhardskill, name="addhardskills"),
    path('about/', views.About, name="about"),
    path('deletesoftskill/<softskills_Description>', views.deletesoftskill, name="deletesoftskill"),
    path('deletehardskill/<hardskills_Description>', views.deletehardskill, name="deletehardskill"),
    path('searchedskills', views.Skill, name="searchedskills"),
    path('updatesoftskill/<softskills_Description>', views.updatesoftskill, name="updatesoftskill"),
    path('updatehardskill/<hardskills_Description>', views.updatehardskill, name="updatehardskill"),
    path('halo/', views.Halo, name="halo"),
    path('canelos/', views.Canelos, name="canelos"),
    path('neguen/', views.Neguen, name="neguen"),
    path('contact/', contact_view.as_view(), name="contact"),
]