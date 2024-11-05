# Generated by Django 5.1.2 on 2024-11-05 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(max_length=100)),
                ('race_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='racetiming',
            name='BIB',
        ),
        migrations.AddField(
            model_name='racedata',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.race'),
        ),
        migrations.AddField(
            model_name='racetiming',
            name='race',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='race_timings', to='api.race'),
            preserve_default=False,
        ),
    ]
