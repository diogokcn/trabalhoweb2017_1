from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import DVD

class IndexView(generic.ListView):
	template_name = 'dvd/index.html'
	context_object_name = 'all_dvd'

	def get_queryset(self):
		return DVD.objects.all()

class DetailView(generic.DetailView):
	model = DVD
	template_name = 'dvd/detail.html'