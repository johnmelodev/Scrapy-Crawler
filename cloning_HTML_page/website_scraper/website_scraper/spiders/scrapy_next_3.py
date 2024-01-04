import scrapy


class QuotesToReadSpider(scrapy.Spider):
    # identity
    name = 'quotebot3'

    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'phrase': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall()
            }

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
