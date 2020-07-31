import django_filters

from .models import *

class OptionFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="date", lookup_expr='gte', label='Start Date', required='True')
    end_date = django_filters.DateTimeFilter(field_name="date", lookup_expr='lte')
    asset_name = django_filters.CharFilter(field_name='asset', lookup_expr='icontains')
    strike = django_filters.NumberFilter(field_name='strike', lookup_expr='exact')
    expmonth = django_filters.NumberFilter(field_name='expmonthyear', lookup_expr='month')
    expyear = django_filters.NumberFilter(field_name='expmonthyear', lookup_expr='year')


    class Meta:
        model = Option
        fields = []
	