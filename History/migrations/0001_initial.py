# Generated by Django 3.2 on 2021-04-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('MovieName', models.CharField(max_length=100)),
                ('MovieGenre', models.CharField(max_length=100)),
                ('MoviePrice', models.IntegerField(max_length=20)),
                ('RentalStart', models.DateField()),
                ('RentalEnd', models.DateField()),
            ],
        ),
    ]
