# -*- coding: utf-8 -*-

# Define here the loaders for your items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/loaders.html

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from {{cookiecutter.project_slug}}.items import {{cookiecutter.scrapy_project_main_class}}Item


class {{cookiecutter.scrapy_project_main_class}}ItemLoader(ItemLoader):
    default_item_class = {{cookiecutter.scrapy_project_main_class}}Item
    default_output_processor = TakeFirst()
