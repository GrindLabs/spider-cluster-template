# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_jsonschema.item import JsonSchemaItem
from {{cookiecutter.project_slug}}.utils import load_schema


class {{cookiecutter.scrapy_main_class}}Item(JsonSchemaItem):
    # Load the schema from the JSON file located in the schemas folder
    # jsonschema = load_schema("example")
    pass
