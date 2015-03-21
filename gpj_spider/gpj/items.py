# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class GpjItem(Item):
    # define the fields for your item here like:
    # name = Field()
    licenseTime = Field()
    mileage = Field()
    price = Field()
    title = Field()
    img = Field()
    transmission = Field()
    tags = Field()
    url = Field()
    type = Field()
