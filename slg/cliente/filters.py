import django_filters

from .models import *


class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['usuario']
