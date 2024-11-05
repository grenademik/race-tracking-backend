from django.db import models

class RaceData(models.Model):
    BIB = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    category = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.BIB} - {self.name}"

class RaceTiming(models.Model):
    BIB = models.ForeignKey(RaceData, on_delete=models.CASCADE, related_name='timings')
    timestamp = models.DateTimeField(auto_now_add=True)
    checkpoint_number = models.PositiveIntegerField()

    def __str__(self):
        return f"BIB: {self.BIB.BIB}, Checkpoint: {self.checkpoint_number}, Time: {self.timestamp}"