from django.urls import path
from BaseFinalProjectApp import views

urlpatterns = [
    path('', views.Home, name=""),
    path('home/', views.Home, name="home"),
    path('experience/', views.Experience, name="experience"),
    path('certifications/', views.Certifications, name="certifications"),
    path('skills/', views.Skill, name="skills"),
    path('addsoftskills/', views.AddSoftSkill, name="addsoftskills"),
    path('addhardskills/', views.AddHardSkill, name="addhardskills"),
    path('about/', views.About, name="about"),
]
