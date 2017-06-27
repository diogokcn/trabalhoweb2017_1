from django.conf.urls import url
from . import views

app_name = 'jogo'

urlpatterns = [
	# /jogo/
    url(r'^$', views.IndexView.as_view(), name='index'),

   # /jogo/<id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /jogo/add
    url(r'^add/$', views.JogoCreate.as_view(), name='jogo-add'),

    # /jogo/edit/<id>/
    url(r'^/edit/(?P<pk>[0-9]+)/$', views.JogoUpdate.as_view(), name='jogo-update'),

    #/jogo/<id>/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', views.JogoDelete.as_view(), name='jogo-delete'),
]
