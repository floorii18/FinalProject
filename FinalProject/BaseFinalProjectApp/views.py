from django.shortcuts import render, redirect
from .models import SoftSkills, HardSkills
from .forms import *

def Home(request):
    contexto = { "form" :  SoftSkillSearch(),
                 "form" : HardSkillSearch()
                 }       
    return render(request, 'home.html' , contexto)

def Experience(request):
   return render(request,'experience.html')

def Certifications(request):
    return render(request,'certifications.html')

def Skill(request):
    if request.POST:

        contexto = {"SoftFilter" : SoftSkills.objects.filter( Description__icontains = request.POST["Description"] ),
                     "HardFilter" : HardSkills.objects.filter( Description__icontains = request.POST["Description"] ) }
        return render(request,'searchedskills.html' , contexto )
    
    else:
        contexto = { "SoftSkills" : SoftSkills.objects.all() , 
                     "HardSkills" : HardSkills.objects.all() , 
                    }

    return render(request,'skills.html' , contexto )

def About(request):
    return render(request,'about.html')

def AddSoftSkill(request):
   return render(request,'addsoftskills.html')

def AddHardSkill(request):
   return render(request,'addhardskills.html')

def addsoftskill(request):
    if request.method == "POST":
        form = SoftSkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = SoftSkillsForm()

    return render(request, 'addsoftskills.html', {'skillform': form})

def addhardskill(request):
    if request.method == "POST":
        form = HardSkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = HardSkillsForm()

    return render(request, 'addhardskills.html', {'skillform': form})

def deletesoftskill(request, softskills_Description):
    softskills = SoftSkills.objects.get(Description=softskills_Description)
    softskills.delete()
    
    softskills = SoftSkills.objects.all()
    context = {"softskills" : softskills}
    
    return render(request, "skills.html", context)

def deletehardskill(request, hardskills_Description):
    hardskills = SoftSkills.objects.get(Description=hardskills_Description)
    hardskills.delete()
    
    hardskills = SoftSkills.objects.all()
    context = {"hardskills" : hardskills}
    
    return render(request, "skills.html", context)
