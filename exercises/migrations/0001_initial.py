# Generated by Django 5.0.4 on 2024-05-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.FloatField()),
                ('exercise_name', models.CharField(max_length=100)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
            ],
        ),
    ]
