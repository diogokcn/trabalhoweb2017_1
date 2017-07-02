from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import JogoEletronico

class IndexView(generic.ListView):
	template_name = 'jogo_eletronico/index.html'
	context_object_name = 'all_jogos'

	def get_queryset(self):
		return JogoEletronico.objects.all()


class DetailView(generic.DetailView):
	model = JogoEletronico
	template_name = 'jogo_eletronico/detail.html'

class JogoCreate(CreateView):
	model = JogoEletronico
	fields = ['titulo', 'estudio', 'distribuidor',
	'genero', 'ano', 'preco']

class JogoUpdate(UpdateView):
	model = JogoEletronico
	fields = ['titulo', 'estudio', 'distribuidor',
	'genero', 'ano', 'preco']


class JogoDelete(DeleteView):
	model = JogoEletronico
	success_url = reverse_lazy('jogo:index')