from BaseFinalProjectApp.models import Certification
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import os

@receiver(pre_save, sender=Certification)
def delete_certification_file(sender, instance, **kwargs):
    # Verificar si ya existe un objeto Avatar en la base de datos
    try:
        old_certification = Certification.objects.get()
    except Certification.DoesNotExist:
        old_certification = None
    # Eliminar el archivo de avatar cuando se borra el objeto Avatar
    if old_certification and old_certification.image:
        old_path = old_certification.image.path
        if os.path.isfile(old_path):
            os.remove(old_path)