from django.db import models

class Race(models.Model):
    race_name = models.CharField(max_length=100)
    race_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.race_name

    def create_race_data(self, bib, name, country, gender, category, age):
        # Create a RaceData instance linked to this Race
        return RaceData.objects.create(
            race=self, 
            BIB=bib, 
            name=name, 
            country=country, 
            gender=gender, 
            category=category, 
            age=age
        )

    def create_race_timing(self, checkpoint_data):
        # Create associated RaceTiming instances for the checkpoints
        for checkpoint in checkpoint_data:
            RaceTiming.objects.create(race=self, checkpoint_number=checkpoint)
        return True


class RaceData(models.Model):
    race = models.ForeignKey(Race, null=True, blank=True, on_delete=models.CASCADE)
    BIB = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    category = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.BIB} - {self.name} (Race: {self.race.race_name})"


class RaceTiming(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='race_timings')  # Direct link to Race
    timestamp = models.DateTimeField(auto_now_add=True)
    checkpoint_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Race: {self.race.race_name}, Checkpoint: {self.checkpoint_number}, Time: {self.timestamp}"
