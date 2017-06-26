from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    url(r'^', views.homepage, name='index'),
    
]
