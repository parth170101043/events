# Generated by Django 2.2 on 2019-04-08 07:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(help_text='Enter the event name', max_length=300)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular event', primary_key=True, serialize=False)),
                ('fee', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('target_audience', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('faq', models.TextField()),
                ('tags', models.CharField(max_length=300)),
            ],
        ),
    ]