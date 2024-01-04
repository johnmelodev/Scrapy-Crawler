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


class ItemsCitation(scrapy.Item):
    # If there is information that you don't want to format the data, don't put in the lines below.
    # input: informs how the incoming data will be processed and how the outgoing data will be exported
    phrase = scrapy.Field(
        input_processor=MapCompose(
            remove_white_space, process_special_characters),
        output_processor=TakeFirst()
    )

    author = scrapy.Field()
    # To join the tags by a comma and not skip lines, use the code below:
    tags = scrapy.Field(
        output_processor=Join(',')
    )

# return your spider and pass the imports from scrapy.loader import ItemLoader
