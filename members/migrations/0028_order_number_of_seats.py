# Generated by Django 5.0.1 on 2024-01-14 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0027_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number_of_seats',
            field=models.IntegerField(default=0),
        ),
    ]
