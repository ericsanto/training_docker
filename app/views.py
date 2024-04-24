from django.shortcuts import render
from django.http import HttpResponse    
from http import HTTPStatus

def home(request):
    return render(request, 'home.html')


def sanit_kubernetes(request):
    return render(request, 'success.html')