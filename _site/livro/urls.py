from django.conf.urls import url
from . import views

app_name = 'livro'

urlpatterns = [
    # /livro/
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    # /livro/<id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /livro/add
    url(r'^add/$', views.LivroCreate.as_view(), name='livro-add'),

    # /livro/edit/<id>/
    url(r'^edit/(?P<pk>[0-9]+)/$', views.LivroUpdate.as_view(), name='livro-update'),

    #/livro/<id>/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', views.LivroDelete.as_view(), name='livro-delete'),

    #/livro/search/
    url(r'^search/$', views.search, name='livro-search'),
]
