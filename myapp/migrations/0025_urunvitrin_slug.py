# Generated by Django 4.2.11 on 2024-06-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_urunler_vitrin_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunvitrin',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
