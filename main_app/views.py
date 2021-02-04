from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Client, Skill
from .forms import ApplicationForm
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
    clients = Client.objects.filter(user=request.user)
    return render(request, 'clients/index.html', { 'clients': clients })

@login_required
def clients_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    skills_client_doesnt_have = Skill.objects.exclude(id__in = client.skills.all().values_list('id'))
    application_form = ApplicationForm()
    return render(request, 'clients/detail.html', { 'client': client, 'application_form': application_form, 'skills': skills_client_doesnt_have })

@login_required
def add_application(request, client_id):
    form = ApplicationForm(request.POST)
    if form.is_valid():
        new_application = form.save(commit=False)
        new_application.client_id = client_id
        new_application.save()
    return redirect('detail', client_id=client_id)

def assoc_skill(request, client_id, skill_id):
    Client.objects.get(id=client_id).skills.add(skill_id)
    return redirect('detail', client_id=client_id)

class SkillList(ListView):
    model = Skill

class SkillDetail(DetailView):
    model = Skill

class SkillCreate(CreateView):
    model = Skill
    fields = ['name', 'experience']

class SkillUpdate(UpdateView):
    model = Skill
    fields = ['name', 'experience']

class SkillDelete(DeleteView):
    model = Skill
    success_url = '/skills/'

class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client 
    fields = ['name', 'title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
