__author__ = 'wpexia'

from scrapy.spider import BaseSpider as Spider
from scrapy.selector import HtmlXPathSelector

from gpj.items import GpjItem

class gpjSpider(Spider):
    name = "gpjSpider"
    allowed_domains = ["http://www.xin.com/"]
    start_urls = [
        "http://www.xin.com/quanguo/s/o2a2i1v1/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        cars = hxs.select('//div[contains(@class,"car-vtc")]');
        for car in cars:
            item = GpjItem()
            item['title'] = car.select('div[contains(@class,"vtc-info")]/p/a/text()').extract()
            item['licenseTime'] = car.select('div[contains(@class,"vtc-info")]/div[contains(@class,"box")]/ul/li[1]/text()').extract()

            items.append(item)
        return items