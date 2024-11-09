from django.db import models


class Race(models.Model):
    race_name = models.CharField(max_length=100)
    race_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.race_name


class RaceData(models.Model):
    race = models.ForeignKey(Race,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    bib = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,
                              choices=[('Male', 'Male'), ('Female', 'Female')])
    category = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.bib} - {self.name} (Race: {self.race.race_name})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["race", "bib"],
                name="unique_race_bib",
            ),
        ]


class RaceTiming(models.Model):
    runner = models.ForeignKey(
        RaceData, on_delete=models.CASCADE,
        related_name='race_timings')  # Direct link to Race
    timestamp = models.DateTimeField(null=True, blank=True)
    checkpoint_number = models.PositiveIntegerField()

    def __str__(self):
        return (f"Race: {self.runner.race.race_name}, Checkpoint: "
                f"{self.checkpoint_number}, Time: {self.timestamp}")
