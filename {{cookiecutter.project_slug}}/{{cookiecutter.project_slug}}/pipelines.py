# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class {{cookiecutter.scrapy_project_main_class}}Pipeline(object):
    """
    This is just an example pipeline, please rename it accordingly to your 
    needs.
    """
    def process_item(self, item, spider):
        return item
