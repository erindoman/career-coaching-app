# Generated by Django 3.1.5 on 2021-02-03 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
    ]
