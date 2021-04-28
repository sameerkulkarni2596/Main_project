from django.db import models

# Create your models here.
class History(models.Model):
    customerName = models.CharField(max_length=100)
    MovieName = models.CharField(max_length=100)
    MovieGenre = models.CharField(max_length=100)
    MoviePrice = models.IntegerField(max_length=20)
    RentalStart = models.DateField()
    RentalEnd = models.DateField()
