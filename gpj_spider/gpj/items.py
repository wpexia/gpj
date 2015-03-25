# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from django.db import models

class GpjItem(models.Model):
    # define the fields for your item here like:
    # name = Field()
    licenseTime = models.DateField()
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=100)
    transmission = models.CharField(max_length=20)
    url = models.URLField()
    type = models.CharField(max_length=20)
    tags = models.CharField(max_length=500)
    no = models.IntegerField()
    class Meta:
        db_table = "seacher_car"
