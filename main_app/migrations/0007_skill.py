# Generated by Django 3.1.6 on 2021-02-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210204_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('softSkills', models.CharField(max_length=20)),
                ('hardSkills', models.CharField(max_length=20)),
            ],
        ),
    ]