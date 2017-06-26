from django.conf.urls import url
from . import views

app_name = 'camiseta'

urlpatterns = [
	# /camiseta/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /camiseta/<pk>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
