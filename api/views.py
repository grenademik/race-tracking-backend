from rest_framework import generics
from .models import RaceData, RaceTiming
from .serializers import RaceDataSerializer, RaceTimingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # RaceData URLs
        'RaceData List': '/racedata-list/',
        'RaceData Detail View': '/racedata-detail/<str:pk>/',
        'RaceData Create': '/racedata-create/',
        'RaceData Update': '/racedata-update/<str:pk>/',
        'RaceData Delete': '/racedata-delete/<str:pk>/',

        # RaceTiming URLs
        'RaceTiming List': '/racetiming-list/',
        'RaceTiming Detail View': '/racetiming-detail/<str:pk>/',
        'RaceTiming Create': '/racetiming-create/',
        'RaceTiming Update': '/racetiming-update/<str:pk>/',
        'RaceTiming Delete': '/racetiming-delete/<str:pk>/',
    }
    return Response(api_urls)


class RaceDataList(generics.ListAPIView):
    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer

class RaceDataDetail(generics.RetrieveAPIView):
    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer

class RaceDataCreate(generics.CreateAPIView):
    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer

class RaceDataUpdate(generics.UpdateAPIView):
    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer

class RaceDataDelete(generics.DestroyAPIView):
    queryset = RaceData.objects.all()
    serializer_class = RaceDataSerializer

    
class RaceTimingList(generics.ListAPIView):
    queryset = RaceTiming.objects.all()
    serializer_class = RaceTimingSerializer

class RaceTimingDetail(generics.RetrieveAPIView):
    queryset = RaceTiming.objects.all()
    serializer_class = RaceTimingSerializer

class RaceTimingCreate(generics.CreateAPIView):
    queryset = RaceTiming.objects.all()
    serializer_class = RaceTimingSerializer

class RaceTimingUpdate(generics.UpdateAPIView):
    queryset = RaceTiming.objects.all()
    serializer_class = RaceTimingSerializer

class RaceTimingDelete(generics.DestroyAPIView):
    queryset = RaceTiming.objects.all()
    serializer_class = RaceTimingSerializer
