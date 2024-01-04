import scrapy
from scrapy.loader import ItemLoader
from website_scraper.items import ItemsCitation


class QuotesToReadSpider(scrapy.Spider):
    # identity
    name = 'quotebot4'

    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            loader = ItemLoader(item=ItemsCitation(),
                                selector=quote, response=response)
            loader.add_xpath('phrase', ".//span[@class='text']/text()")
            loader.add_xpath('author', ".//small[@class='author']/text()")
            loader.add_xpath('tags', ".//div[@class='tags']/a/text()")
            yield loader.load_item()

        try:
            next_page_link = response.xpath(
                "//li[@class='next']/a/@href").get()
            if next_page_link is not None:
                full_next_page_url = response.urljoin(
                    next_page_link)
                yield scrapy.Request(
                    url=full_next_page_url, callback=self.parse)
        except:
            print('We have reached the last page')
