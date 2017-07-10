from .models import DVD
import django_filters

class DVDFilter(django_filters.FilterSet):  
	class Meta:
		model  = DVD
		fields = ['titulo']