from RegisterFinalProjectApp.models import Avatar
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import os

@receiver(pre_save, sender=Avatar)
def delete_avatar_file(sender, instance, **kwargs):
    # Verificar si ya existe un objeto Avatar en la base de datos
    try:
        old_avatar = Avatar.objects.get(user=instance.user)
    except Avatar.DoesNotExist:
        old_avatar = None
    # Eliminar el archivo de avatar cuando se borra el objeto Avatar
    if old_avatar and old_avatar.image:
        old_path = old_avatar.image.path
        if os.path.isfile(old_path):
            os.remove(old_path)