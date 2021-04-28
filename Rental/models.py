from django.db import models

# Create your models here.

class Rentals(models.Model):
    OrderId = models.IntegerField(primary_key=True)
    RentalStart = models.DateField()
    RentalEnd = models.DateField()

