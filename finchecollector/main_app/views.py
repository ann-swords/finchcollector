from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# Classes:
class FinchCreate(CreateView):
  model = Finch
  fields = "__all__"
  success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ["breed", "description", "age"]
  success_url = '/finches/'

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  finches_list = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches_list})

def finches_details(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', {'finch': finch})

