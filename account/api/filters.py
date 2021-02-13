import django_filters
from django.db.models import Q
from ..models import StudentProfile

class StudentFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='custom_search')

    class Meta:
        model = StudentProfile
        fields = ['search']

    def custom_search(self,queryset,name,value):
        return queryset.filter(
            Q(user__username__icontains=value)
        )