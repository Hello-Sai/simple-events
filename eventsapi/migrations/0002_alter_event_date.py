# Generated by Django 4.0.4 on 2024-03-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
