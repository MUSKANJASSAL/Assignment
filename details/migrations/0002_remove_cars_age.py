# Generated by Django 3.0.7 on 2020-06-09 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='age',
        ),
    ]