__author__ = 'wpexia'

from scrapy.spider import BaseSpider as Spider
from scrapy.selector import HtmlXPathSelector


class gpjSpider(Spider):
    name = "gpjSpider"
    allowed_domains = ["http://www.xin.com/"]
    start_urls = [
        "http://www.xin.com/quanguo/s/o2a2i1v1/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        filename = "a.txt"
        sites = hxs.select('//div[contains(@class,"vtc-info")]/p');
        for site in sites:
            print site.extract()
            #open(filename, "wb").write(site.select('a/text()').extract())