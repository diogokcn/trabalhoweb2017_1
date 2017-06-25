from django.http import HttpResponse
from django.template import loader
from .models import Livro

def index(request):
    todos_livros = Livro.objects.all()
    template = loader.get_template('livro/index.html')
    context  = {
        'todos_livros': todos_livros,
    }
    return HttpResponse(template.render(context, request))

def detail(request, livro_id):
    return HttpResponse("<h2> Detalhes do Livro de ID " + str(livro_id) + "</h2>")
