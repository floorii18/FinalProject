# Generated by Django 4.2 on 2023-10-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entity', models.CharField(max_length=50)),
                ('Duration', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=50, unique=True)),
                ('Level', models.PositiveIntegerField()),
            ],
        ),
    ]
