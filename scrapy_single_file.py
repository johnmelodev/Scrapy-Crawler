import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesToScrapeSpider(scrapy.Spider):
    # Identity
    name = 'quotebot'
    # Request

    def start_requests(self):
        # Define url(s) to scrape
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response

    def parse(self, response):
        # this is where you should process what is returned from the response
        for element in response.xpath("//div[@class='quote']"):
            yield {
                'phrase': element.xpath(".//div[@class='quoteText']/text()").get(),
                'author': element.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tags': element.xpath(".//div[@class='greyText smallText left']/a/text()").getall()
            }


bot = CrawlerProcess(
    settings={
        "FEEDS": {
            "items.csv": {"format": "csv"}
        }
    }
)

bot.crawl(QuotesToScrapeSpider)
bot.start()
