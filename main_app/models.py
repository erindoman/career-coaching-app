from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'client_id': self.id})
