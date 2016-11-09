# -*- coding: utf-8 -*-
import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["test.com"]
    start_urls = (
        'http://www.test.com/',
    )

    def parse(self, response):
        pass
