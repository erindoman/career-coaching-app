from django.contrib import admin
from .models import Client, Application, Skill

# Register your models here.
admin.site.register(Client)
admin.site.register(Application)
admin.site.register(Skill)