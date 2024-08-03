# Generated by Django 5.0.7 on 2024-08-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="description",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
