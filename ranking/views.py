from django.shortcuts import render
from django.views import generic
from .models import swordfighter

class swordfighterList(generic.ListView):
    model = swordfighter
    template_name = 'index.html'
    paginate_by = 6
