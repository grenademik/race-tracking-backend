from rest_framework import serializers
from .models import RaceData, RaceTiming

class RaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceData
        fields = '__all__'

class RaceTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceTiming
        fields = '__all__'
