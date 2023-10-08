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
    
    context = {}
    
    if request.POST:
        description = request.POST["Description"]
        SoftFilter = SoftSkills.objects.filter(Description__icontains=description)
        HardFilter = HardSkills.objects.filter(Description__icontains=description)

        if not SoftFilter and not HardFilter:
            message = "No results found."
            context = {"message": message}
        
        else:
            message = ""
            context = {"SoftFilter": SoftFilter,
                        "HardFilter": HardFilter,
                        "message": message
                        }
        return render(request, 'searchedskills.html', context)
    
    else:
        context = { "SoftSkills" : SoftSkills.objects.all() , 
                     "HardSkills" : HardSkills.objects.all() , 
                    }
        return render(request,'skills.html' , context )

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
    hardskills = HardSkills.objects.get(Description=hardskills_Description)
    hardskills.delete()
    
    hardskills = HardSkills.objects.all()
    context = {"hardskills" : hardskills}
    
    return render(request, "skills.html", context)
