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
from .models import Person, Photo, Interest

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'cwr-photobucket'

@login_required(login_url='/accounts/login/')
def home(request):
  return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/accounts/login/')
def person_index(request):
    people = Person.objects.all()
    return render(request, 'people/index.html', { 'people': people })

@login_required(login_url='/accounts/login/')
def person_detail(request, person_id):
    person = Person.objects.get(id=person_id)
    interests = Interest.objects.all()
    return render(request, 'people/detail.html', { 
        'person': person,
        'interests': interests
    })

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
    fields = ['name', 'bio', 'instagram', 'twitter', 'discord']
    success_url = '/people/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['bio', 'instagram', 'twitter', 'discord']

class PersonDelete(LoginRequiredMixin, DeleteView):
    model= Person
    success_url = '/people'

class InterestCreate(LoginRequiredMixin, CreateView):
    model = Interest
    fields = ['name']
    success_url='/interests/'

class InterestDelete(LoginRequiredMixin, DeleteView):
    model = Interest
    success_url = '/interests/'

class InterestList(LoginRequiredMixin, ListView):
    model = Interest
    template_name = 'interests/index.html'

@login_required
def assoc_interest(request, person_id, interest_id):
    Person.objects.get(id=person_id).interests.add(interest_id)
    return redirect('detail', person_id=person_id)

@login_required
def assoc_interest_delete(request, person_id, interest_id):
    Person.objects.get(id=person_id).interests.remove(interest_id)
    return redirect('detail', person_id=person_id)

@login_required(login_url='/accounts/login/')
def interest_detail(request, interest_id):
    people = Person.objects.all()
    interest = Interest.objects.get(id = interest_id)
    return render(request, 'interests/detail.html', { 
        'people': people,
        'interest': interest
    })

@login_required
def add_photo(request, person_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, person_id=person_id)
      photo.save()
    except Exception as error:
      print("Error uploading photo: ", error)
      return redirect('detail', person_id=person_id)
  return redirect('detail', person_id=person_id)
