from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = (
    ('A', 'Applied'),
    ('R', 'Rejected'),
    ('O', 'Offer'),
    ('I', 'Interviewing')
)

class Skill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skills_detail', kwargs={'pk': self.id})

class Client(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'client_id': self.id})

class Application(models.Model):
    title = models.CharField(max_length=500)
    dateApplied = models.DateField('Date Applied')
    company = models.CharField(max_length=100)
    link = models.URLField()
    status = models.CharField(
        max_length = 1,
        choices = STATUS,
        default = STATUS[0][0]
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_status_display()} on {self.dateApplied}'

    class Meta:
        ordering = ['-dateApplied']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for client_id: {self.client_id} @{self.url}"