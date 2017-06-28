from django.conf.urls import url
from . import views

app_name = 'camiseta'

urlpatterns = [
	# /camiseta/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /camiseta/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /camiseta/add
    url(r'^add/$', views.CamisetaCreate.as_view(), name='camiseta-add'),

    # /camiseta/edit/<id>/
    url(r'^/edit/(?P<pk>[0-9]+)/$', views.CamisetaUpdate.as_view(), name='camiseta-update'),

    #/camiseta/<id>/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', views.CamisetaDelete.as_view(), name='camiseta-delete'),
]
