from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import JogoEletronico
from .filters import JogoFilter

def search(request):
    Jogo_list   = JogoEletronico.objects.all()
    Jogo_filter = JogoFilter(request.GET, queryset=Jogo_list)
    return render(request, 'jogo_eletronico/jogo_list.html', {'filter': Jogo_filter})

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

	def form_valid(self, form):
		JogoEletronico = form.save(commit=False)
		JogoEletronico.user = self.request.user
		return super(JogoCreate, self).form_valid(form)

class JogoUpdate(UpdateView):
	model = JogoEletronico
	fields = ['titulo', 'estudio', 'distribuidor',
	'genero', 'ano', 'preco']


class JogoDelete(DeleteView):
	model = JogoEletronico
	success_url = reverse_lazy('jogo:index')