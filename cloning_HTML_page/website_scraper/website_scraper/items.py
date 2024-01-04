# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join


def tirar_espaco_em_branco(valor):
    return valor.strip()


def processar_caracteres_especiais(valor):
    return valor.replace(u"\u201c", '').replace(u"\u201d", '').replace(u"\u2014", '—')


class ItemsCitation(scrapy.Item):
    # If there is an infomation that you don't want to format the data. don't put in the lines below.
    # input: informs how the incoming data will be processed and how the outgoing data will be exported
    phrase = scrapy.Field(
        input_processor=MapCompose(
            tirar_espaco_em_branco, processar_caracteres_especiais),
        output_processor=TakeFirst()
    )

    author = scrapy.Field()
    # Para unir as tags por uma virgula e nao pular linhas use o codigo abaixo:
    tags = scrapy.Field(
        output_processor=Join(',')
    )

# retorne a sua spider e passe as importacoes from scrapy.loader import ItemLoader
