from django.shortcuts import render, redirect
from .models import SoftSkills, HardSkills
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from RegisterFinalProjectApp.models import Avatar

def Home(request):

    contexto = { "form" :  SoftSkillSearch(),
                 "form" : HardSkillSearch(),} 
      
    return render(request, 'home.html' , contexto)

def Experience(request):
   return render(request,'experience.html')

def Halo(request):
    return render(request, 'Halo.html')

def Canelos(request):
    return render(request, 'Canelos.html')

def Neguen(request):
    return render(request, 'Neguen.html')

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

def updatesoftskill(request, softskills_Description):
    
    softskills = SoftSkills.objects.get(Description=softskills_Description)
    
    if request.method == 'POST':
        form = SoftSkillsForm(request.POST)
        print(form)
        
        if form.is_valid:
            information = form.cleaned_data
            softskills.Description = information['Description']
            softskills.Level = information['Level']
            form.save()
            
        return render(request, 'skills.html')
    
    else:
        form = SoftSkillsForm(initial={'Description' : softskills.Description, 'Level' : softskills.Level})
        
    return render(request, 'updatesoftskill.html', {"form" : form, "softskills_Desciption" : softskills_Description})

def updatehardskill(request, hardskills_Description):
    
    hardskills = HardSkills.objects.get(Description=hardskills_Description)
    
    if request.method == 'POST':
        form = HardSkillsForm(request.POST)
        print(form)
        
        if form.is_valid:
            information = form.cleaned_data
            hardskills.Description = information['Description']
            hardskills.Level = information['Level']
            form.save()
            
        return render(request, 'skills.html')
    
    else:
        form = HardSkillsForm(initial={'Description' : hardskills.Description, 'Level' : hardskills.Level})
        
    return render(request, 'updatehardskill.html', {"form" : form, "hardskills_Desciption" : hardskills_Description})

class contact_view(LoginRequiredMixin, CreateView):
    model = ContactForm
    form_class = ContactFormModelForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def Certifications(request):
    certifications = Certification.objects.all()
    context = {"certifications": certifications}
    return render(request, 'certifications.html', context)
 
def AddCertification(request):
    if request.method == "POST":
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certifications')
    else:
        form = CertificationForm()
    context = {"form": form}
    return render(request, 'addCertification.html', context)

def DeleteCertification(request, certification_title):
    certification = Certification.objects.get(title=certification_title)
    certification.delete()
    
    certification = Certification.objects.all()
    context = {"certification" : certification}
    
    return render(request, "certifications.html", context)

def UpdateCertification(request, certification_title):
    
    certification = Certification.objects.get(title=certification_title)
    
    if request.method == 'POST':
        form = Certification(request.POST)
        print(form)
        
        if form.is_valid:
            information = form.cleaned_data
            certification.title = information['title']
            certification.description = information['description']
            certification.image = information['image']
            form.save()
            
        return render(request, 'certifications.html')
    
    else:
        form = CertificationForm(initial={'title' : certification.title,
                                          'description' : certification.description, 
                                          'image' : certification.image})
        
    return render(request, 'updateCertifications.html', {"form" : form, "certification_title" : certification_title})