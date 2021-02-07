from django.contrib import admin
from .models import Client, Application, Skill, Photo

# Register your models here.
admin.site.register(Client)
admin.site.register(Application)
admin.site.register(Skill)
admin.site.register(Photo)