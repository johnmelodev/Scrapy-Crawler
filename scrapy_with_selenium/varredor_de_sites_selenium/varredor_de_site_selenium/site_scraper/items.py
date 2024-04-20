# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def remove_white_space(value):
    return value.strip()


def process_special_characters(value):
    return value.replace(u"\u201c", '').replace(u"\u201d", '').replace(u"\u2014", '—')


class QuoteItem(scrapy.Item):
    phrase = scrapy.Field(
        input_processor=MapCompose(
            remove_white_space, process_special_characters),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(',')
    )


def remove_quotes(value):
    return value.replace(u"\u2019", '')


def make_uppercase(value):
    return value.upper()


class GoodReadsQuoteItem(scrapy.Item):
    phrase = scrapy.Field(
        input_processor=MapCompose(remove_white_space, remove_quotes),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_white_space, make_uppercase),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(';'),
    )
