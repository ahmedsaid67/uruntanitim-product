# Generated by Django 4.2.11 on 2024-06-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hakkimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
