# Generated by Django 3.2 on 2021-04-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0002_alter_rentals_rentalend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='OrderId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
