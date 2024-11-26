import os
import django
import pandas as pd

# Set the Django settings module to your project’s settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raceTracking.settings')  # Make sure 'raceTracking.settings' is correct

# Initialize Django
django.setup()

# Now import models
from api.models import Race, RaceData

# Your CSV processing and data import logic
df = pd.read_csv('data.csv')
race = Race.objects.get(id=1)

for index, row in df.iterrows():
    print(f"{index + 1}/{len(df)}")
    RaceData.objects.create(
        race=race,
        bib=row['BIB'],
        name=row['FULL NAME'],
        country=row['COUNTRY'],
        gender=row['GEN'],
        category=row['DISTANCE'],
        age=row['AGE'],
    )

print("Data imported successfully!")
