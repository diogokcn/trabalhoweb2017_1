from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Camiseta

class IndexView(generic.ListView):
	template_name = 'camiseta/index.html'
	context_object_name = 'all_camiseta'

	def get_queryset(self):
		return Camiseta.objects.all()

class DetailView(generic.DetailView):
	model = Camiseta
	template_name = 'camiseta/detail.html'

# Camiseta's CRUD
# Create
class CamisetaCreate(CreateView):
	model = Camiseta
	fields = ['marca', 'tamanho', 'cor', 'tecido', 'preco']

# Update
class CamisetaUpdate(UpdateView):
	model = Camiseta
	fields = ['marca', 'tamanho', 'cor', 'tecido', 'preco']

# Delete
class CamisetaDelete(DeleteView):
	model = Camiseta
	success_url = reverse_lazy('camiseta:index')