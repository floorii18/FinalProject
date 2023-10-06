# Generated by Django 4.2 on 2023-10-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseFinalProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50, unique=True)),
                ('Level', models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='HardSkills',
        ),
    ]
