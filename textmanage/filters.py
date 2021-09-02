import django_filters

from .models import *

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = employee
        fields = '__all__'

class PartyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = party
        fields = ['party_name', 'party_id', 'gst_number',]

class SalaryReportFilter(django_filters.FilterSet):
    name =  django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = wages_report
        fields = ['employee_id', 'bill_number',]

class MachineReportFilter(django_filters.FilterSet):
    name =  django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = maintenance_inventory
        fields = ['machine_id', 'bill_id',]

class OrdersFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = party_bill_delivery
        fields = '__all__'
