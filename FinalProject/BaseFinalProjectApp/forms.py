from django import forms
from .models import *

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