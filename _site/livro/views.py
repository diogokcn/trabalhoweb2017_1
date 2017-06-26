from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Livro


class IndexView(generic.ListView):
	template_name = 'livro/index.html'
	context_object_name = 'all_livro'

	def get_queryset(self):
		return Livro.objects.all()


class DetailView(generic.DetailView):
	model = Livro
	template_name = 'livro/detail.html'


class LivroCreate(CreateView):
	model = Livro
	fields = ['titulo', 'ano', 'editora',
	'autora', 'nroPags', 'formato', 'preco']

class LivroUpdate(UpdateView):
	model = Livro
	fields = ['titulo', 'ano', 'editora',
	'autora', 'nroPags', 'formato', 'preco']


class LivroDelete(DeleteView):
	model = Livro
	success_url = reverse_lazy('livro:index')


#class UserFormVIew(View):