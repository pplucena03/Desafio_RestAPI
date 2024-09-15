from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    summary = filters.CharFilter(field_name='summary', lookup_expr='icontains')
    start_date = filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['summary', 'start_date', 'end_date']