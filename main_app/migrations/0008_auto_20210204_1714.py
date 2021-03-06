# Generated by Django 3.1.6 on 2021-02-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='hardSkills',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='softSkills',
        ),
        migrations.AddField(
            model_name='client',
            name='skills',
            field=models.ManyToManyField(to='main_app.Skill'),
        ),
    ]
