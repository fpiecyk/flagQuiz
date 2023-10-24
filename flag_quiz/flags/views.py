from django.shortcuts import render
from .models import FlagData

# Create your views here.

def home(request):
    poland = FlagData.objects.get(short_name = 'pl')
    return render(request, 'home.html', {'poland': poland})