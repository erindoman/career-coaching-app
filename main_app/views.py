from django.shortcuts import render
from .models import Client

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def clients_index(request):
    clients = Client.objects.all()
    return render(request, 'clients/index.html', { 'clients': clients })