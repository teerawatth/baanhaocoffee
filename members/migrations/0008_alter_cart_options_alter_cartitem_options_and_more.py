# Generated by Django 5.0.1 on 2024-01-08 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_cart_cartitem_cart_foods'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['id'], 'verbose_name': 'ตะกร้า', 'verbose_name_plural': 'ตะกร้า'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['id'], 'verbose_name': 'รายการ', 'verbose_name_plural': 'รายการ'},
        ),
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
