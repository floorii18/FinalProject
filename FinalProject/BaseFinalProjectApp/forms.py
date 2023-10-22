from django import forms
from .models import *
from django.core.exceptions import ValidationError

class SoftSkillsForm(forms.ModelForm):
    class Meta:
	#Aquí indicamos el modelo que queremos usar.
        model = SoftSkills
	#Aquí tenemos que pasar todas las variables con las que cuenta nuestro modelo.
        fields = ['Description', 'Level']

    
class HardSkillsForm(forms.ModelForm):
    class Meta:
	#Aquí indicamos el modelo que queremos usar.
        model = HardSkills
	#Aquí tenemos que pasar todas las variables con las que cuenta nuestro modelo.
        fields = ['Description', 'Level']
        
class SoftSkillSearch(forms.ModelForm):

    class Meta:
        model = SoftSkills
        fields = ["Description"]
        
class HardSkillSearch(forms.ModelForm):

    class Meta:
        model = HardSkills
        fields = ["Description"]
        
        
class CertificationForm(forms.ModelForm):
        class Meta:
         model = Certification
         fields = ['title', 'description', 'image']
         
class ContactFormModelForm(forms.ModelForm):
        subject = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

        class Meta:
                model = ContactForm
                fields = ['name', 'email', 'subject', 'message']
                widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                }
                labels = {
                'name': ('Your Name'),
                'email': ('Your Email'),
                'subject': ('Recipient'),
                'message': ('Message'),
                }
                help_texts = {
                'name': ('Please enter your full name.'),
                'email': ('Please enter a valid email address.'),
                'subject': ('Select the recipient of your message.'),
                'message': ('Enter your message here.'),
                }

        def clean_email(self):
                email = self.cleaned_data.get('email')
                if "example.com" in email:
                        raise ValidationError(
                                ("Email addresses from example.com are not allowed."),
                                code='invalid',
                                params={'email': email},
                        )
                return email