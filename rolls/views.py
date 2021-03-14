from django.http import HttpResponse
from django.shortcuts import render
from .models import Roll


def menu(request):
    rolls = Roll.objects.all()
    return render(request, 'menu.html', {'rolls':rolls})

def contattaci(request):
    return render(request, 'contattaci.html')