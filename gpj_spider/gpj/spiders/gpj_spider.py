# -*- coding: utf-8 -*-
__author__ = 'wpexia'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from gpj.items import GpjItem


class GpjSpider(BaseSpider):
    name = "gpjSpider"
    allowed_domains = ["http://www.xin.com/"]
    start_urls = [
        "http://www.xin.com/quanguo/s/o2a2i1v1/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        number = int(hxs.select('//div[contains(@class,"con-page search_page_link")]/a[last()-1]/text()').extract()[0])
        items = []
        for i in range(1, number):
            build_url = 'http://www.xin.com/quanguo/s/o2a2i%sv1/' % (i)
            items.append(self.make_requests_from_url(build_url).replace(callback=self.parse_index))
        return items

    def parse_index(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select('//div[contains(@class,"car-vtc vtc-border")]/div[contains(@class,"vtc-img")]/a/@href')
        items = []
        for url in urls:
            build_url = 'http://www.xin.com%s' % (url.extract())
            items.append(self.make_requests_from_url(build_url).replace(callback=self.parse_page))
        return items

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response)
        item = GpjItem()
        item['licenseTime'] = hxs.select('//ul[contains(@class,"contit")]/li[1]/em/text()').extract()
        item['mileage'] = hxs.select('//ul[contains(@class,"contit")]/li[2]/em/text()').extract()
        item['price'] = hxs.select('//div[contains(@class,"wan_1")]/em/text()').extract()
        item['title'] = hxs.select('//div[contains(@class,"tit")]/h1/text()').extract()
        item['img'] = hxs.select('//div[contains(@class,"d-photo img-album")]/a/img/@src').extract()
        item['url'] = response.url
        item['tags'] = {}
        importants = hxs.select('//div[contains(@class,"configur")]/ul/li')
        imp = []
        for important in importants:
            text = important.select('span/text()').extract()
            if text:
                imp.append(text)
        item['tags'][u"配置亮点"] = imp
        item['transmission'] = hxs.select('//div[contains(@class,"param clearfix")]/div[2]/table/tr[1]/td[2]/text()').extract()
        item['type'] = hxs.select('//div[contains(@id,"ulover")]/div[2]/div[2]/table/tr[1]/td[2]/text()').extract()
        return item
