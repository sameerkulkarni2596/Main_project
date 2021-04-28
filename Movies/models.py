from django.db import models

# Create your models here.

class Movies(models.Model):
    MovieId = models.AutoField(primary_key= True)
    MovieName = models.CharField(max_length= 100)
    MovieGenre = models.CharField(max_length = 100)
    MoviePrice = models.IntegerField(max_length = 20)
