from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
    
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s - %s' % (self.name, self.message)

class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certifications/', null=True, blank = True)

    def __str__(self):
        return f"{self.image} /n {self.title} \n {self.description}"