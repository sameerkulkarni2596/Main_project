# Generated by Django 3.0.5 on 2021-04-28 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210428_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
