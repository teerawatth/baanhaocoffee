# Generated by Django 5.0.1 on 2024-01-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='foods/'),
        ),
        migrations.AlterField(
            model_name='pets',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='pets/'),
        ),
    ]
