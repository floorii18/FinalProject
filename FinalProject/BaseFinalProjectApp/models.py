from django.db import models

class Certifications(models.Model):
    Entity=models.CharField(max_length=50)
    Duration=models.CharField(max_length=50)
    Description=models.CharField(max_length=5000)
    
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
