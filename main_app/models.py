from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    joined = models.DateField()