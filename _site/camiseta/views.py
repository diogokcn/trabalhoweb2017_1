from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Camiseta

class IndexView(generic.ListView):
	template_name = 'camiseta/index.html'
	context_object_name = 'all_camiseta'

	def get_queryset(self):
		return Camiseta.objects.all()

class DetailView(generic.DetailView):
	model = Camiseta
	template_name = 'camiseta/detail.html'