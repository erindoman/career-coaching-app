from django.contrib import admin
from .models import Client, Application

# Register your models here.
admin.site.register(Client)
admin.site.register(Application)