from .models import Camiseta
import django_filters

class CamisetaFilter(django_filters.FilterSet):  
	class Meta:
		model  = Camiseta
		fields = ['marca']