# Generated by Django 3.0.5 on 2021-04-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0003_alter_rentals_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='OrderId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]