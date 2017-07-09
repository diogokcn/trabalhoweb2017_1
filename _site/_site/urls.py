"""_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from home import views
from django.contrib import admin

# I8n URLs
urlpatterns = i18n_patterns(
    url(r'^$',               'home.views.index'),
    url(r'^admin/',          include(admin.site.urls)),
    url(r'^accounts/',       include('django.contrib.auth.urls')),
    url(r'^home/',           include('home.urls', namespace='home')),
    url(r'^user/',           include('user.urls', namespace='user')),
    url(r'^livro/',          include('livro.urls', namespace='livro')),
    url(r'^camiseta/',       include('camiseta.urls', namespace='camiseta')),
    url(r'^dvd/',            include('dvd.urls', namespace='dvd')),
    url(r'^jogoeletronico/', include('jogo_eletronico.urls', namespace='jogo')),
    url(r'^comments/',       include('django_comments.urls')),
)
