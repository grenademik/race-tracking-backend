import pandas as pd
from api.models import Race, RaceData

df = pd.read_csv('data.csv')

race = Race.objects.get(id=3)

for index, row in df.iterrows():
    print(f"{index}/{len(df)}")
    RaceData.objects.create(race=race,
                            bib=row['BIB'],
                            name=row['FULL NAME'],
                            country=row['COUNTRY'],
                            gender=row['GEN'],
                            category=row['DISTANCE'],
                            age=row['AGE'])

print("Data imported successfully!")
