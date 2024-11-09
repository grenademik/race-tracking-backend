from django_filters.filterset import FilterSet
from rest_framework.viewsets import ModelViewSet

from api.models import Race, RaceData, RaceTiming
from api.serializers import (RaceDataSerializer, RaceSerializer,
                             RaceTimingSerializer)


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


class RaceTimingAPI(ModelViewSet):
    queryset = RaceTiming.objects.all().order_by('-id')
    serializer_class = RaceTimingSerializer
    filterset_class = RaceTimingFilterSet
