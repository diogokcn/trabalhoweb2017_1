from django.http import HttpResponse
from django.template import loader
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


'''
def index(request):
    todos_livros = Livro.objects.all()
    template = loader.get_template('livro/index.html')
    context  = {
        'todos_livros': todos_livros,
    }
    return HttpResponse(template.render(context, request))

def detail(request, livro_id):
    return HttpResponse("<h2> Detalhes do Livro de ID " + str(livro_id) + "</h2>")
'''