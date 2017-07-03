from django.shortcuts import render, render_to_response
from django.views import generic
from django.template import RequestContext

def homepage(request):
	return render(request, 'home/index.html', {})

def index(request):
    return render_to_response('home/index.html')