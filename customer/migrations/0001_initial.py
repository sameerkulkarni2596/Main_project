# Generated by Django 3.2 on 2021-04-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('cardnumber', models.IntegerField(max_length=16)),
                ('phonenumber', models.IntegerField(max_length=10)),
            ],
        ),
    ]
