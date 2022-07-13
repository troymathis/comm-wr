from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

import uuid
import boto3
from .models import Person

@login_required(login_url='/accounts/login/')
def home(request):
  return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    def get_success_url(self, request, user):
        return "/upload/new"

    return render(request, 'registration/signup.html', context)

class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['bio', 'instagram', 'twitter', 'discord']
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def add_photo(request, person_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid().hex[:6] + photo_file.name[photo_file.name.rifind]