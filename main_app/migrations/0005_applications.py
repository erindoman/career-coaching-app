# Generated by Django 3.1.6 on 2021-02-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_client_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('dateApplied', models.DateField(verbose_name='Date Applied')),
                ('company', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('status', models.CharField(choices=[('A', 'Applied'), ('R', 'Rejected'), ('O', 'Offer'), ('I', 'Interviewing')], default='A', max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.client')),
            ],
            options={
                'ordering': ['-dateApplied'],
            },
        ),
    ]
