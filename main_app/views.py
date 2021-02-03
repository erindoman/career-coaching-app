from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def clients_index(request):
    clients = Client.objects.all()
    return render(request, 'clients/index.html', { 'clients': clients })

@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/detail.html', { 'client': client })

class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client 
    fields = '__all__'

class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'

class ClientDelete(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = '/clients/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
