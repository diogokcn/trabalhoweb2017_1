from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy
from .models import DVD

class IndexView(generic.ListView):
	template_name = 'dvd/index.html'
	context_object_name = 'all_dvd'

	def get_queryset(self):
		return DVD.objects.all()

class DetailView(generic.DetailView):
	model = DVD
	template_name = 'dvd/detail.html'

# DVD's CRUD
# Create
class DVDCreate(CreateView):
	model = DVD
	fields = ['titulo', 'genero', 'ano', 'duracao', 'preco']
	
	def form_valid(self, form):
		DVD = form.save(commit=False)
		DVD.user = self.request.user
		return super(DVDCreate, self).form_valid(form)
		
# Update
class DVDUpdate(UpdateView):
	model = DVD
	fields = ['titulo', 'genero', 'ano', 'duracao', 'preco']

# Delete
class DVDDelete(DeleteView):
	model = DVD
	success_url = reverse_lazy('dvd:index')