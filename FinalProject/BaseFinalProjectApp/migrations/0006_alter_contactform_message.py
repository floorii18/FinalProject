# Generated by Django 4.2.5 on 2023-10-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseFinalProjectApp', '0005_alter_contactform_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(),
        ),
    ]
