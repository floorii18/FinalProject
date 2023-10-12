from django.db import models
from django.contrib.auth.models import AbstractUser
    
    
class User(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users_groups',
        related_query_name='custom_users_group',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        related_query_name='custom_user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Usar User personalizado
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    @property
    def d(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user} - {self.image}"
