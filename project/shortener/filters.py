import django_filters as filter
from django_filters import DateFilter
from .models import URLS


class URLFilter(filter.FilterSet):
    start_date = DateFilter(field_name='retrieve_time', lookup_expr='gte')
    end_date = DateFilter(field_name='retrieve_time', lookup_expr='lte')

    class Meta:
        model = URLS
        fields = '__all__'
        exclude = ['user', 'retrieve_time', 'short_url']
        widget = {

        }
