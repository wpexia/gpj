# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class GpjSpiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    licenseTime = Field()
    mileage = Field()
    transmission = Field()
    city = Field()
    newCar = Field()
    price = Field()
    cheap = Field()
    title = Field()
    img = Field()
    accident = Field()
    phone = Field()
    place = Field()
    tags = Field()