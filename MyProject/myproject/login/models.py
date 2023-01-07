from django.db import models

# Create your models here.

class users(models.Model):
    firtname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    age=models.IntegerField()
    Homeland=models.CharField(max_length=500)
