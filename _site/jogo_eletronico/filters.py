from .models import JogoEletronico
import django_filters

class JogoFilter(django_filters.FilterSet):  
	class Meta:
		model  = JogoEletronico
		fields = ['titulo']