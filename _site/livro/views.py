from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Livro


class IndexView(generic.ListView):
	template_name = 'livro/index.html'
	context_object_name = 'all_livro'

	def get_queryset(self):
		return Livro.objects.all()


class DetailView(generic.DetailView):
	model = Livro
	template_name = 'livro/detail.html'