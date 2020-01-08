import scrapy

from {{cookiecutter.project_slug}}.settings import logger


class DefaultSpider(scrapy.Spider):
    """
    This spider is just a template for the future spiders.
    
    Please, remove it or rename this file and class with the name of your 
    first spider.
    """
    name = 'default'

    def start_requests(self):
        # TODO: The lookup URLs must come from the database
        urls = []

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
