from rest_framework import serializers
from .models import Race, RaceData, RaceTiming

class RaceTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceTiming
        fields = ['checkpoint_number', 'timestamp']  # Include relevant fields for timing

class RaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceData
        fields = ['BIB', 'name', 'country', 'gender', 'category', 'age']

class RaceSerializer(serializers.ModelSerializer):
    race_data = RaceDataSerializer(many=True, source='racedata_set')  # Specify source for RaceData relation
    race_timings = RaceTimingSerializer(many=True)  # No need to specify source here

    class Meta:
        model = Race
        fields = ['race_name', 'race_date', 'location', 'race_data', 'race_timings']



    def create(self, validated_data):
        # Extract nested race_data and race_timings from validated data
        race_data_list = validated_data.pop('race_data')
        race_timings_list = validated_data.pop('race_timings')
        
        # Create the Race instance
        race_instance = Race.objects.create(**validated_data)

        # Create RaceData instances linked to the Race instance
        for race_data in race_data_list:
            RaceData.objects.create(race=race_instance, **race_data)

        # Create RaceTiming instances directly linked to the Race instance
        for timing_data in race_timings_list:
            RaceTiming.objects.create(race=race_instance, **timing_data)

        return race_instance
