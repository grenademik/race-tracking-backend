from django_filters.filterset import FilterSet
from rest_framework.viewsets import ModelViewSet

from api.models import Race, RaceData, RaceTiming
from api.serializers import (RaceDataSerializer, RaceSerializer,
                             RaceTimingSerializer)

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class RaceFilterSet(FilterSet):

    class Meta:
        model = Race
        fields = "__all__"


class RaceAPI(ModelViewSet):
    queryset = Race.objects.all().order_by('-id')
    serializer_class = RaceSerializer
    filterset_class = RaceFilterSet
    search_fields = ['race_name']


class RaceDataFilterSet(FilterSet):

    class Meta:
        model = RaceData
        fields = "__all__"


class RaceDataAPI(ModelViewSet):
    queryset = RaceData.objects.all().order_by('-id')
    serializer_class = RaceDataSerializer
    filterset_class = RaceDataFilterSet


class RaceTimingFilterSet(FilterSet):

    class Meta:
        model = RaceTiming
        fields = "__all__"


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class RaceTimingAPI(ModelViewSet):
    queryset = RaceTiming.objects.all().order_by('-id')
    serializer_class = RaceTimingSerializer
    filterset_class = RaceTimingFilterSet
    pagination_class = CustomPageNumberPagination
