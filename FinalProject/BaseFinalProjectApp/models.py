from django.db import models
    
class SoftSkills(models.Model):
    Description=models.CharField(max_length=50, unique=True)
    Level=models.PositiveIntegerField()
    
    def __str__(self):
        return f" {self.Description} - Level: {self.Level}"
    
class HardSkills(models.Model):
    Description=models.CharField(max_length=50, unique=True)
    Level=models.PositiveIntegerField()
    
    def __str__(self):
        return f" {self.Description} - Level: {self.Level}"
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)

class Certification(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/certifications/')
    
    def __str__(self):
        return f"{self.image} /n {self.title} \n {self.description}"