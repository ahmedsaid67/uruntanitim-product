# Generated by Django 4.2.11 on 2024-04-23 01:03

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_sliders'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrunKategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('kapak_fotografi', models.ImageField(blank=True, null=True, upload_to=myapp.models.kapakfoto_path_urunkategori)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UrunVitrin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=255)),
                ('fiyat', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('kapak_fotografi', models.ImageField(blank=True, null=True, upload_to=myapp.models.kapakfoto_path_urunler)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('urun_kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.urunkategori')),
                ('vitrin_kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.urunvitrin')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=myapp.models.album_path_fotogaleri)),
                ('durum', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('urun', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.urunler')),
            ],
        ),
    ]
