# Generated by Django 4.2.11 on 2024-06-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_urunler_baslik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunler',
            name='fiyat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
