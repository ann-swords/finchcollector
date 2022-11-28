from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})


def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

