from django.shortcuts import render
from django.views import generic

def homepage(request):
	return render(request, 'home/index.html', {})