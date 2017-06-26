from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Pagina de Jogos Eletronicos </h2>")
