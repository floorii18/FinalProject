# Generated by Django 4.2.5 on 2023-10-08 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BaseFinalProjectApp', '0002_softskills_rename_skills_hardskills'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certifications',
        ),
    ]