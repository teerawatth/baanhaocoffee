# Generated by Django 5.0.1 on 2024-01-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0030_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='imgcovers/')),
            ],
        ),
    ]