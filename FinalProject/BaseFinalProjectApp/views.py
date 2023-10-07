from django.shortcuts import render, redirect
from .models import SoftSkills, HardSkills
from .forms import SoftSkillsForm, HardSkillsForm

def Home(request):
    context = {}
    if request.method == "POST":
        context = {"FilterSoftSkill" : SoftSkills.objects.filter(Description_icontains = request.POST["search"]),
                   "FilterSoftSkill" : HardSkills.objects.filter(Description_icontains = request.POST["search"])
                   } 
        return redirect("skills")   
    
    return render(request, 'home.html', context)

def Experience(request):
   return render(request,'experience.html')

def Certifications(request):
    return render(request,'certifications.html')

def Skill(request):
   contexto = {
        "SoftSkills": SoftSkills.objects.all(),
        "HardSkills": HardSkills.objects.all()
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

