# Generated by Django 3.0.5 on 2021-04-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0005_auto_20210428_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='OrderId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]