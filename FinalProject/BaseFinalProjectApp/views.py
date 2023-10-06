from django.shortcuts import render
from .models import SoftSkills, HardSkills
from .forms import SoftSkillsForm, HardSkillsForm

def Home(request):
    return render(request, 'home.html')

def Experience(request):
   return render(request,'experience.html')

def Certifications(request):
    return render(request,'certifications.html')

def Skill(request):
   return render(request,'skills.html')

def About(request):
    return render(request,'about.html')

def AddSoftSkill(request):
   return render(request,'addsoftskills.html')

def AddHardSkill(request):
   return render(request,'addhardskills.html')


def addsoftskill(request):
    if request.method == "POST":
        form = SoftSkillsForm(request.POST['Description'], request.POST['Level'])
        print(form)
        if form.is_valid():
            skillinfo = form.cleaned_data
            skillinfo = SoftSkills(Description=skillinfo['Description'], Level=skillinfo['Level'])
            skillinfo.save()
            return render(request,'skills.html')
    else:
        form = SkillsForm()
    return render(request,'addsoftskills.html', {'form':form})

def addhardskill(request):
    if request.method == "POST":
        form = HardSkillsForm(request.POST['Description'], request.POST['Level'])
        print(form)
        if form.is_valid():
            skillinfo = form.cleaned_data
            skillinfo = HardSkills(Description=skillinfo['Description'], Level=skillinfo['Level'])
            skillinfo.save()
            return render(request,'skills.html')
    else:
        form = SkillsForm()
    return render(request,'addhardskills.html', {'form':form})
