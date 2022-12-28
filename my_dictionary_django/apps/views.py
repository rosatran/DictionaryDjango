from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

def apps(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())

def search(request):
    return HttpResponse("Hello world!")