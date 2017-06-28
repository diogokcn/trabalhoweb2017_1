from django.conf.urls import url
from . import views

app_name = 'dvd'

urlpatterns = [
	# /dvd/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /dvd/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /dvd/add
    url(r'^add/$', views.DVDCreate.as_view(), name='dvd-add'),

    # /dvd/edit/<id>/
    url(r'^/edit/(?P<pk>[0-9]+)/$', views.DVDUpdate.as_view(), name='dvd-update'),

    #/dvd/<id>/delete/
    url(r'(?P<pk>[0-9]+)/delete/$', views.DVDDelete.as_view(), name='dvd-delete'),
]
