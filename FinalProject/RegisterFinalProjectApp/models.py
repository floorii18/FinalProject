from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='avatars', null=True, blank = True)

    @property
    def d(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user} - {self.image}"
    
    
class User (models.Model):
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=10)
