from django.db import models

# Create your models here.
class Car(models.Model):
    licenseTime = models.DateField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=100)
    transmission = models.IntegerField()
    url = models.URLField()
    type = models.IntegerField()
    tags = models.CharField(max_length=500)
    no = models.IntegerField()