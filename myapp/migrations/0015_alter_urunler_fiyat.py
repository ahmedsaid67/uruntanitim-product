# Generated by Django 4.2.11 on 2024-06-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_urunler_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunler',
            name='fiyat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
