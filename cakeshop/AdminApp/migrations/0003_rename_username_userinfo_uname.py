# Generated by Django 4.1.1 on 2022-11-25 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='uname',
        ),
    ]
