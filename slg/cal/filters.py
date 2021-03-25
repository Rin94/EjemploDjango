import django_filters

from .models import *


class CalFilter(django_filters.FilterSet):
    # start_date= DateTimeFilter(field_name="start_date")
    # end_date = DateTimeFilter(field_name="end_date")
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['usuario']
