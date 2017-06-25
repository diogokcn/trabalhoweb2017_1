from django.http import HttpResponse
from .models import Livro

def index(request):
    todos_Livros = Livro.objects.all()
    html = ''
    for livro in todos_Livros:
        url  = '/livro/' + str(livro.id) + '/'
        html += '<a href="' + url + '">' + livro.titulo + '</a><br>'  
    return HttpResponse(html)

def detail(request, livro_id):
    return HttpResponse("<h2> Detalhes do Livro de ID " + str(livro_id) + "</h2>")
