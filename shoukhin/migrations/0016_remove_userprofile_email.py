# Generated by Django 5.0.3 on 2024-05-03 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoukhin', '0015_userprofile_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
