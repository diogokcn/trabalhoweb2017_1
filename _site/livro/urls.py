from django.conf.urls import url
from . import views

urlpatterns = [
    # /livro/
    url(r'^$', views.index, name='index'),

    # /livro/<id>/
    url(r'^(?P<livro_id>[0-9]+)/$', views.detail, name='detail'),
]
