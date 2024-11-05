import csv
import io
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Race, RaceData, RaceTiming
from .serializers import RaceSerializer, RaceDataSerializer, RaceTimingSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # Race URLs
        'Race List': '/races/',
        'Race Detail View': '/races/<str:pk>/',
        'Race Create': '/races/create/',
        'Race Update': '/races/update/<str:pk>/',
        'Race Delete': '/races/delete/<str:pk>/',

        # Nested RaceData URLs within a specific Race
        'RaceData List': '/races/<str:race_pk>/data/',
        'RaceData Detail View': '/races/<str:race_pk>/data/<str:pk>/',
        'RaceData Create': '/races/<str:race_pk>/data/create/',
        'RaceData Update': '/races/<str:race_pk>/data/update/<str:pk>/',
        'RaceData Delete': '/races/<str:race_pk>/data/delete/<str:pk>/',

        # RaceTiming URLs directly linked to Race
        'RaceTiming List': '/races/<str:race_pk>/timings/',
        'RaceTiming Detail View': '/races/<str:race_pk>/timings/<str:pk>/',
        'RaceTiming Create': '/races/<str:race_pk>/timings/create/',
        'RaceTiming Update': '/races/<str:race_pk>/timings/update/<str:pk>/',
        'RaceTiming Delete': '/races/<str:race_pk>/timings/delete/<str:pk>/',
        
        # RaceData CSV Upload URL
        'RaceData Upload': '/races/<str:race_pk>/data/upload/',
    }
    return Response(api_urls)

# Race Views
class RaceList(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceDetail(generics.RetrieveAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceCreate(generics.CreateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceUpdate(generics.UpdateAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class RaceDelete(generics.DestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

# RaceData Views - Nested within a Race
class RaceDataList(generics.ListAPIView):
    serializer_class = RaceDataSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceData.objects.filter(race__id=race_pk)

class RaceDataDetail(generics.RetrieveAPIView):
    serializer_class = RaceDataSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceData.objects.filter(race__id=race_pk)

class RaceDataCreate(generics.CreateAPIView):
    serializer_class = RaceDataSerializer

    def perform_create(self, serializer):
        race_pk = self.kwargs['race_pk']
        race = Race.objects.get(id=race_pk)
        serializer.save(race=race)

class RaceDataUpdate(generics.UpdateAPIView):
    serializer_class = RaceDataSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceData.objects.filter(race__id=race_pk)

class RaceDataDelete(generics.DestroyAPIView):
    serializer_class = RaceDataSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceData.objects.filter(race__id=race_pk)

# New RaceData Upload View
class RaceDataUpload(generics.CreateAPIView):
    serializer_class = RaceDataSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        race_pk = kwargs['race_pk']
        file = request.FILES['file']

        if not file.name.endswith('.csv'):
            return JsonResponse({'error': 'File is not a CSV'}, status=400)

        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string, delimiter=',')
        
        race_data_list = []
        
        headers = next(reader)  # Assuming the first row is the header
        
        for row in reader:
            race_data = {}
            for header, value in zip(headers, row):
                race_data[header] = value
            
            race_data['race'] = race_pk  # Assuming 'race' is the ForeignKey field
            
            race_data_list.append(race_data)

        serializer = self.get_serializer(data=race_data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data, status=201)

# RaceTiming Views - Linked directly to Race
class RaceTimingList(generics.ListAPIView):
    serializer_class = RaceTimingSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceTiming.objects.filter(race_data__race__id=race_pk)

class RaceTimingDetail(generics.RetrieveAPIView):
    serializer_class = RaceTimingSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceTiming.objects.filter(race_data__race__id=race_pk)

class RaceTimingCreate(generics.CreateAPIView):
    serializer_class = RaceTimingSerializer

    def perform_create(self, serializer):
        race_pk = self.kwargs['race_pk']
        race = Race.objects.get(id=race_pk)
        serializer.save(race_data=race)

class RaceTimingUpdate(generics.UpdateAPIView):
    serializer_class = RaceTimingSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceTiming.objects.filter(race_data__race__id=race_pk)

class RaceTimingDelete(generics.DestroyAPIView):
    serializer_class = RaceTimingSerializer

    def get_queryset(self):
        race_pk = self.kwargs['race_pk']
        return RaceTiming.objects.filter(race_data__race__id=race_pk)
