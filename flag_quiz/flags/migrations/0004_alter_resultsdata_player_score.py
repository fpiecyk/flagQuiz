# Generated by Django 4.2.5 on 2023-10-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0003_resultsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsdata',
            name='player_score',
            field=models.IntegerField(blank=True),
        ),
    ]
