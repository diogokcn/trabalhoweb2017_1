from .models import Livro
import django_filters

class LivroFilter(django_filters.FilterSet):  
	class Meta:
		model  = Livro
		fields = ['titulo']