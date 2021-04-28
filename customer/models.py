from django.db import models

# Create your models here.
class customer(models.Model):
    customerId = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    zipcode = models.IntegerField(max_length=5)
    cardnumber = models.IntegerField(max_length=16)
    phonenumber = models.IntegerField(max_length=10)
