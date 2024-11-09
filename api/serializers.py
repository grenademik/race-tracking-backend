from rest_framework import serializers
from .models import Race, RaceData, RaceTiming


class RaceTimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaceTiming
        fields = '__all__'


class RaceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaceData
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = '__all__'
