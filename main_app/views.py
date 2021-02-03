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
    # clients = Client.objects.filter(user=request.user)
    clients = Client.objects.all()
    return render(request, 'clients/index.html', { 'clients': clients })

@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/detail.html', { 'client': client })

class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client 
    fields = '__all__'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
