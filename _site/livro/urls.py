from django.conf.urls import url
from . import views

app_name = 'livro'

urlpatterns = [
    # /livro/
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    # /livro/<id>/
    url(r'^(?P<livro_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
