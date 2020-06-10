# Generated by Django 3.0.7 on 2020-06-09 18:42

import details.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('vehicle', models.CharField(max_length=50)),
                ('transmission', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('engine_no', models.CharField(max_length=70)),
                ('color', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=details.models.Cars.upload_img)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.Vehicle')),
            ],
        ),
    ]