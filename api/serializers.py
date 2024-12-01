from rest_framework import serializers
from .models import Race, RaceData, RaceTiming
from rest_framework.serializers import CharField


class RaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = '__all__'


class RaceDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaceData
        fields = '__all__'


class RaceTimingSerializer(serializers.ModelSerializer):
    runner_details = RaceDataSerializer(source='runner', read_only=True)
    runner_bib = CharField(required=False, write_only=True)

    def create(self, validated_data):
        runner_bib = validated_data.pop('runner_bib', None)  # Use default None
        runner = RaceData.objects.get(bib=runner_bib)
        validated_data['runner'] = runner
        return super().create(validated_data)

    class Meta:
        model = RaceTiming
        fields = '__all__'
