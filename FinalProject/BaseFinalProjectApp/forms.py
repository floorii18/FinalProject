from django import forms

class SoftSkillsForm(forms.Form):
    Description = forms.CharField()
    Level = forms.CharField()
    
class HardSkillsForm(forms.Form):
    Description = forms.CharField()
    Level = forms.CharField()